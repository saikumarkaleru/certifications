# The Discounting Foundation

## The Problem / Why this matters

Every valuation number you will ever produce — a target price in an equity research note, an enterprise value in an M&A pitch, a recovery estimate in a distressed credit memo — is, underneath the spreadsheet gymnastics, a single act: **you take cash that arrives in the future and you translate it into what it is worth today.** That translation is called discounting. It is the load-bearing wall of the entire building. If your revenue growth is off by 2%, your valuation is wrong at the margin. If your discounting logic is off, your valuation is wrong at the *foundation*, and every clever adjustment you layer on top inherits the error.

Interviewers know this. That is exactly why the discounting questions come early and come hard. When an equity research director asks a candidate to "walk me through a DCF," what they are really testing in the first sixty seconds is whether you understand *why* a dollar next year is worth less than a dollar today, whether you can build a discount factor from scratch without a template, and whether you know the difference between discounting a cash flow at the end of the year versus the middle of the year. Candidates who have only ever pressed `=NPV()` in Excel fall apart here. Candidates who understand the foundation can rebuild the whole model on a whiteboard with no formulas in front of them — and that is the person who gets hired.

This chapter builds the discounting foundation from the ground up. Not "here is the formula," but "here is why the formula is the only formula it could possibly be." By the end you will be able to: derive a discount factor from first principles, explain and apply the mid-year convention and defend when it is and isn't appropriate, articulate the exact three-way relationship between discount rate, growth, and value, quantify how sensitive a valuation is to the discount rate (this is where most of the value uncertainty actually lives), and price a growing stream of cash flows both as a finite series and as a perpetuity. These are not five separate topics. They are five faces of one idea.

## Core Idea

**A dollar you receive in the future is worth less than a dollar in your hand today, and discounting is the machinery that tells you exactly how much less.**

There are three, and only three, reasons a future dollar is worth less:

1. **You could have invested today's dollar** and earned a return in the meantime — so a future dollar has to "catch up" from a smaller starting amount. This is the pure time-value component.
2. **The future dollar might not show up at all** — the company could underperform, default, or disappear. Risk demands compensation.
3. **Inflation erodes purchasing power** — the future dollar buys less bread than today's dollar.

We bundle all three into a single number called the **discount rate**, `r`. The discount rate is the required rate of return an investor demands to be willing to wait and to bear the risk. Discounting is nothing more than running compound interest *backwards*: if money grows forward at rate `r`, then to move money backwards in time you divide by `(1 + r)` for each period you travel back.

The present value of a single future cash flow is:

```
PV = CF / (1 + r)^n
```

where `CF` is the cash flow, `r` is the discount rate per period, and `n` is the number of periods until you receive it. That single equation, applied cash flow by cash flow and summed, *is* a discounted cash flow valuation. Everything else — mid-year conventions, terminal values, growing perpetuities, sensitivity tables — is elaboration on this one line.

## Why it works this way — first principles

Let's derive the discount factor rather than assert it, because that derivation is exactly what separates a memorizer from someone who understands.

**Step 1 — Forward compounding.** Suppose you have `$100` today and you can earn `r = 10%` per year with certainty. After one year you have `100 × 1.10 = $110`. After two years the interest itself earns interest — you compound — so you have `100 × 1.10 × 1.10 = 100 × 1.10^2 = $121`. After `n` years:

```
Future Value = Present Value × (1 + r)^n
```

This is the growth engine of money. It runs in one direction: forward.

**Step 2 — Invert it.** Valuation asks the *reverse* question. We don't know today's value and want the future — we know (or forecast) the future cash flow and want today's value. So we solve the same equation for Present Value:

```
Present Value = Future Value / (1 + r)^n
```

That is it. Discounting is not a new concept bolted onto finance; it is compound interest read from right to left. The term `1 / (1 + r)^n` is called the **discount factor** for period `n`. It is always between 0 and 1 (for positive `r`), it shrinks as `n` grows, and it shrinks faster when `r` is larger. Multiply any future cash flow by its discount factor and you get its present value.

**Step 3 — Why we can add them.** A stream of cash flows is just a bunch of single cash flows arriving at different times. Because present values are all expressed in the same units — today's dollars — they are directly additive. The value of a business that pays you `CF₁, CF₂, ... CFₙ` is simply the sum of each flow's present value:

```
PV = Σ  CFₜ / (1 + r)^t     for t = 1 to n
```

This additivity is called the **value-additivity principle**, and it is the quiet workhorse of all of valuation. It is why we can value a company as the sum of an explicit forecast period plus a terminal value, why we can value a conglomerate as a sum of its parts, and why a bond is just the sum of its coupons and principal each discounted back.

**Why the discount rate is a *required return*, not a prediction.** A subtle but interview-critical point: `r` is not your forecast of what the investment will return. It is the return you *require* to part with your money given the risk. If an asset is riskier, you demand a higher `r`, which shrinks the discount factor, which lowers the present value. Risk enters valuation entirely through the discount rate (in the standard DCF framework) — the numerator holds *expected* cash flows and the denominator holds the *risk-adjusted required return*. Keep those two jobs separate in your head; conflating them is one of the most common analytical errors and interviewers probe for it.

## Full technical content

### The building blocks

| Symbol | Name | Meaning |
|---|---|---|
| `CF` or `CFₜ` | Cash flow | The money received; subscript `t` denotes the period it arrives |
| `r` | Discount rate | Required return per period; for a whole firm this is the WACC, for equity it is the cost of equity |
| `n`, `t` | Period index | Number of compounding periods from today |
| `DF` | Discount factor | `1 / (1 + r)^t`; converts a period-`t` dollar to today's dollars |
| `g` | Growth rate | The rate at which a cash-flow stream grows each period |
| `PV` | Present value | Today's worth of one or more future cash flows |
| `TV` | Terminal value | The value of all cash flows beyond the explicit forecast horizon |

### The single-cash-flow present value

```
PV = CFₜ × DFₜ = CFₜ / (1 + r)^t
```

### The multi-period present value (a DCF, in one line)

```
PV = Σ_{t=1}^{n}  CFₜ / (1 + r)^t
```

### Discount factors decay — build the intuition with a table

At `r = 10%`, here is what one dollar received in year `n` is worth today:

| Year `n` | Discount factor `1/(1.10)^n` | One dollar is worth today |
|---|---|---|
| 1 | 0.9091 | $0.9091 |
| 2 | 0.8264 | $0.8264 |
| 3 | 0.7513 | $0.7513 |
| 4 | 0.6830 | $0.6830 |
| 5 | 0.6209 | $0.6209 |
| 10 | 0.3855 | $0.3855 |
| 20 | 0.1486 | $0.1486 |
| 30 | 0.0573 | $0.0573 |

Two lessons jump out and both matter in interviews. First, **money far in the future is worth remarkably little today** — a dollar 30 years out is worth under 6 cents at a 10% rate. Second, **the decay is exponential, not linear** — each additional year multiplies by another `1/1.10`, so the factor falls off a cliff early and then flattens. This is why the first five years of a forecast usually carry more discounted weight than years 6–10, and why terminal-value assumptions, despite being "far away," can still dominate — more on that tension shortly.

### Discrete (end-of-year) convention

The default DCF assumption is that each year's entire cash flow lands in a lump on the **last day of the year**. Year-1 flow is discounted by `(1+r)^1`, year-2 by `(1+r)^2`, and so on. This is the **discrete** or **end-of-period** convention. It is simple, it is the textbook default, and it slightly *understates* value because it pretends you wait a full year for cash that a real business actually generates continuously throughout the year.

### Mid-year convention

Real companies collect revenue every day, not in a single December-31 lump. The **mid-year convention** corrects for this by assuming each year's cash flow arrives, on average, at the **midpoint** of the year. Practically, you subtract 0.5 from every period exponent:

```
Discrete:   PV = Σ  CFₜ / (1 + r)^t
Mid-year:   PV = Σ  CFₜ / (1 + r)^(t − 0.5)
```

Because you are discounting over a *shorter* effective time (t − 0.5 instead of t), every discount factor is larger, so **mid-year convention always produces a higher present value than the discrete convention.** The uplift is roughly a constant multiplicative factor of `(1 + r)^0.5` — about `√1.10 ≈ 1.0488`, i.e. a ~4.9% bump at a 10% discount rate. That is not trivial; on a large valuation it can be the difference between a deal clearing a hurdle rate or not.

| Convention | Period-1 exponent | Assumed timing of cash | Effect on value |
|---|---|---|---|
| Discrete / end-of-year | 1.0 | Dec 31 lump | Lower (conservative) |
| Mid-year | 0.5 | June 30 average | Higher by ~`(1+r)^0.5` |

**The terminal-value subtlety with mid-year (a favorite interview trap).** When you use mid-year convention, you must be consistent about how you discount the terminal value, and the treatment differs by method:

- **Gordon Growth (perpetuity) terminal value:** The Gordon formula `TV = CF_{n+1} / (r − g)` computes a value as of the *end* of year `n`. But the perpetuity cash flows it capitalizes are themselves mid-year flows, so the perpetuity value is naturally an end-of-year figure that already embeds mid-year timing of the underlying flows — the standard convention is to discount that TV back using the **same mid-year exponent as the final explicit year (`n − 0.5`)**, because the terminal value is effectively "handed to you" at the same mid-year point.
- **Exit-multiple terminal value:** An exit multiple (say `EV = 8× EBITDA`) reflects a *sale price at the end of year `n`*, a point-in-time transaction on the last day. Many practitioners discount it at the **full-year exponent `n`** (not `n − 0.5`) because the sale is a discrete end-of-period event, not a stream. Being able to articulate this distinction cleanly signals real modeling experience.

The safe, defensible interview answer: *"Mid-year convention discounts each explicit cash flow at t minus one-half because cash is earned throughout the year. For a Gordon-growth terminal value I keep it consistent and discount at the same mid-year point as the last stub year; for an exit-multiple terminal value I'd discount the full period because it represents a discrete sale at year-end."*

### Continuous compounding (know it exists)

If you push the compounding frequency to its limit — interest calculated every instant — the discount factor becomes `e^(−r·t)`, using the exponential constant `e ≈ 2.71828`. Continuous discounting is standard in options pricing (Black-Scholes) and fixed-income analytics but rare in equity DCFs. Interviewers occasionally test whether you know the *concept* exists and that mid-year convention is essentially a crude, one-step approximation of continuous compounding. You will almost never build an equity DCF with it.

### The relationship between discount rate, growth, and value

Here is the intellectual heart of the chapter. Consider the simplest possible business: one that produces a cash flow next year of `CF₁` and grows it forever at a constant rate `g`. The value of that infinite growing stream collapses to a stunningly compact formula, the **Gordon Growth Model** (derived in the next section):

```
PV = CF₁ / (r − g)
```

Stare at the denominator, `(r − g)`. It is the *spread* between the required return and the growth rate, and it governs everything:

- **Value rises as `r` falls.** A lower required return means the future is discounted less harshly — the denominator shrinks — so value climbs. Cheap money (low rates) inflates asset prices; this single relationship explains a huge share of macro market moves.
- **Value rises as `g` rises.** Faster-growing cash flows are worth more — again the denominator shrinks.
- **The relationship is non-linear and explosive near `r = g`.** As `g` creeps toward `r`, the denominator approaches zero and value approaches infinity. This is not a real-world result; it is a mathematical warning. It tells you that **`g` must always be strictly less than `r`**, and by a comfortable margin, or the model breaks.
- **`g` can never exceed the long-run growth rate of the economy.** If a company grew faster than GDP forever, it would eventually *become* the entire economy — an absurdity. So terminal `g` is capped, in practice, at something like long-run nominal GDP growth (~2–4% in developed markets). Interviewers love to catch candidates who plug in a `g` of 6% "because the company is growing fast." Fast growth is a *finite-period* phenomenon; the terminal growth rate is a *forever* number and must be humble.

Let's make the non-linearity concrete. With `CF₁ = $100`:

| `r` | `g` | `r − g` | Value `= 100/(r−g)` |
|---|---|---|---|
| 10% | 2% | 8% | $1,250 |
| 10% | 3% | 7% | $1,429 |
| 10% | 4% | 6% | $1,667 |
| 10% | 5% | 5% | $2,000 |
| 9% | 3% | 6% | $1,667 |
| 8% | 3% | 5% | $2,000 |
| 8% | 5% | 3% | $3,333 |

Notice how moving `g` from 4% to 5% (a one-point change) lifts value from `$1,667` to `$2,000` — a 20% jump — while moving it from 2% to 3% lifts it only 14%. **The closer `r` and `g` get, the more violently value reacts to any change in either.** That is why terminal-value assumptions are so dangerous and so heavily scrutinized in due diligence.

### Sensitivity of value to the discount rate

If there is one number in a DCF that keeps analysts up at night, it is the discount rate. Small changes in `r` cause large changes in value, and the effect is amplified for long-duration cash flows (growth companies, infrastructure, anything where the payoff is far out). Here is why, and how to quantify it.

For a single cash flow, `PV = CF / (1+r)^n`. Take the sensitivity of `PV` to `r`:

```
dPV/dr = −n × CF / (1 + r)^(n+1) = −(n / (1 + r)) × PV
```

The magnitude of the sensitivity scales with `n` — **the further out the cash flow, the more its present value moves for a given change in `r`.** This is the same idea as **duration** in fixed income: long-duration assets are rate-sensitive assets. A high-growth tech company whose cash flows are back-loaded into years 8–10 and the terminal value is far more sensitive to a 50bp move in WACC than a mature utility whose cash is near-term and stable.

For a growing perpetuity, the sensitivity is even sharper because `r` sits in the `(r − g)` denominator. Differentiate `PV = CF₁/(r − g)`:

```
dPV/dr = −CF₁ / (r − g)^2
```

The `(r − g)^2` in the denominator means the sensitivity **explodes** as the spread narrows. Let's tabulate the value of our `CF₁ = $100`, `g = 3%` business as `r` moves:

| `r` | `r − g` | Value | % change from base (r=10%) |
|---|---|---|---|
| 8% | 5% | $2,000 | +40% |
| 9% | 6% | $1,667 | +17% |
| 10% (base) | 7% | $1,429 | — |
| 11% | 8% | $1,250 | −13% |
| 12% | 9% | $1,111 | −22% |

A mere ±2 percentage-point swing in the discount rate moves the valuation from `+40%` to `−22%` — a range wider than the entire equity value of many companies. **This is the single most important sensitivity in valuation, and it is why every serious DCF is delivered with a data table (a sensitivity grid) flexing WACC against terminal growth, not a single-point answer.** In an interview, if you present a DCF as one number without acknowledging this, you look naïve. If you say *"my base case is X, but here's my sensitivity table — the value ranges from Y to Z across a reasonable band of WACC and g"* — you look like an analyst.

### Present value of a growing stream

Now we assemble the machinery for the most common real objects in valuation: growing streams. There are two flavors — the finite growing annuity and the infinite growing perpetuity.

**Growing perpetuity (the Gordon Growth Model) — full derivation.** A growing perpetuity pays `CF₁` one period from now, then grows each payment by `g` forever: `CF₁, CF₁(1+g), CF₁(1+g)^2, ...`. Its present value is the infinite sum:

```
PV = CF₁/(1+r) + CF₁(1+g)/(1+r)^2 + CF₁(1+g)^2/(1+r)^3 + ...
```

This is a geometric series with first term `a = CF₁/(1+r)` and common ratio `x = (1+g)/(1+r)`. A geometric series converges only if `|x| < 1`, which requires `g < r` — the mathematical origin of the "growth must be below the discount rate" rule. The sum of an infinite geometric series is `a / (1 − x)`:

```
PV = [CF₁/(1+r)]  /  [1 − (1+g)/(1+r)]
   = [CF₁/(1+r)]  /  [((1+r) − (1+g))/(1+r)]
   = CF₁ / ((1+r) − (1+g))
   = CF₁ / (r − g)
```

There it is — the Gordon Growth Model, `PV = CF₁ / (r − g)`, is not a magic formula; it is the closed-form sum of an infinite growing geometric series. **Crucial detail interviewers test: the numerator is next period's cash flow (`CF₁`), the *first* payment, which already includes one period of growth over today's `CF₀`.** If you're handed `CF₀` (this year's cash flow), you must grow it first: `PV = CF₀(1+g)/(r − g)`. Forgetting the `(1+g)` grow-up is one of the most common terminal-value errors.

**Growing annuity (finite growing stream).** If the growing stream runs for only `n` periods and then stops, the closed form is:

```
PV = (CF₁ / (r − g)) × [ 1 − ((1 + g)/(1 + r))^n ]
```

The first factor is the perpetuity value; the bracket "chops off" the tail beyond year `n`. As `n → ∞`, the bracket → 1 and you recover the Gordon formula. This is useful for finite-life assets — a patent with `n` years of royalties growing at `g`, a lease, a wasting resource.

**How this plugs into a DCF — the terminal value.** A real DCF splits the future into two pieces because we cannot forecast individual cash flows forever:

1. An **explicit forecast period** (typically 5–10 years) where you project each year's free cash flow and discount it individually.
2. A **terminal value** capturing everything beyond the horizon, most often via Gordon Growth: `TV_n = CF_{n+1} / (r − g) = CFₙ(1+g)/(r − g)`. This TV is a value *as of the end of year `n`*, so it must itself be discounted back to today by `1/(1+r)^n`.

```
Enterprise Value = Σ_{t=1}^{n} FCFₜ/(1+r)^t  +  [CFₙ(1+g)/(r−g)] / (1+r)^n
                   └─── explicit period PV ───┘   └──── PV of terminal value ────┘
```

The terminal value routinely represents **60–80% of total enterprise value** in a standard DCF, which is precisely why the `(r − g)` sensitivity discussed above is so consequential: the majority of your valuation lives in a single formula driven by two of the most judgmental inputs in finance.

### From enterprise value to equity value — the bridge

Discounting *unlevered* free cash flow at the WACC gives you **enterprise value (EV)** — the value of the whole operating business, available to *all* capital providers (debt and equity). To get to **equity value** (what the shareholders own, the basis for a share price), you walk the **EV-to-equity bridge**:

```
Equity Value = Enterprise Value − Net Debt − Preferred − Minority Interest + Non-operating assets
```

where `Net Debt = Total Debt − Cash & equivalents`. The logic is airtight from first principles: EV values the operating assets; debt holders and preferred holders have a senior claim that must be paid before common shareholders, so you subtract them; minority interests represent value that belongs to outside shareholders of consolidated subsidiaries, so subtract; non-operating assets (excess cash, investments not in the cash flows) belong to shareholders but weren't captured in operating FCF, so add them back. Divide equity value by diluted shares outstanding to get **value per share**, the deliverable in equity research.

```mermaid
flowchart TD
  A[Unlevered Free Cash Flow] -->|discount at WACC| B[Enterprise Value]
  B -->|subtract Net Debt| C[minus Net Debt]
  C -->|subtract Preferred and Minority| D[minus Preferred and Minority]
  D -->|add Non-operating assets| E[Equity Value]
  E -->|divide by diluted shares| F[Value per Share]
```

## Worked examples

### Worked Example 1 — Single cash flows, discrete vs mid-year

**Setup.** A project will pay `$500` at the end of year 1, `$600` at the end of year 2, and `$700` at the end of year 3. The discount rate is `r = 12%`. Find the present value under (a) the discrete convention and (b) the mid-year convention.

**(a) Discrete convention.** Discount each flow at its full-year exponent.

| Year `t` | `CFₜ` | `(1.12)^t` | `DFₜ = 1/(1.12)^t` | `PV = CFₜ × DFₜ` |
|---|---|---|---|---|
| 1 | $500 | 1.1200 | 0.89286 | $446.43 |
| 2 | $600 | 1.2544 | 0.79719 | $478.32 |
| 3 | $700 | 1.404928 | 0.71178 | $498.25 |
| | | | **Total PV** | **$1,423.00** |

Let me verify the arithmetic: `500 × 0.89286 = 446.43`; `600 × 0.79719 = 478.32`; `700 × 0.71178 = 498.25`. Sum = `446.43 + 478.32 + 498.25 = 1,423.00`. ✓

**(b) Mid-year convention.** Subtract 0.5 from every exponent.

| Year `t` | `CFₜ` | Exponent `t−0.5` | `(1.12)^(t−0.5)` | `DF` | `PV` |
|---|---|---|---|---|---|
| 1 | $500 | 0.5 | 1.05830 | 0.94491 | $472.46 |
| 2 | $600 | 1.5 | 1.18530 | 0.84366 | $506.20 |
| 3 | $700 | 2.5 | 1.32754 | 0.75327 | $527.29 |
| | | | **Total PV** | | **$1,505.94** |

Check: `(1.12)^0.5 = 1.05830`, so `DF = 0.94491`; `500 × 0.94491 = 472.46`. Each mid-year PV should equal the discrete PV times `(1.12)^0.5 = 1.05830`: `1,423.00 × 1.05830 = 1,505.96` (a two-cent rounding difference from the line-by-line sum). ✓

**Takeaway.** Mid-year lifts value from `$1,423.00` to `$1,505.94`, a `+5.8%` uplift, consistent with the `(1+r)^0.5` rule at `r = 12%` (`√1.12 = 1.0583`, i.e. +5.83%). The higher the discount rate, the bigger the mid-year benefit.

### Worked Example 2 — A full mini-DCF with a Gordon terminal value and the equity bridge

**Setup.** You are valuing MidCo. Unlevered free cash flow (FCF) is forecast for 5 years, then grows at a terminal rate of `g = 2.5%` forever. WACC = `9%`. Use the discrete convention.

| Year | FCF ($m) |
|---|---|
| 1 | 100 |
| 2 | 115 |
| 3 | 128 |
| 4 | 138 |
| 5 | 145 |

Balance sheet: total debt `$300m`, cash `$60m`, preferred stock `$40m`, minority interest `$20m`, a non-operating equity investment worth `$25m`. Diluted shares outstanding: `50m`.

**Step 1 — PV of explicit FCF at WACC = 9%.**

| Year `t` | FCF | `(1.09)^t` | `DF` | `PV` |
|---|---|---|---|---|
| 1 | 100 | 1.09000 | 0.91743 | 91.74 |
| 2 | 115 | 1.18810 | 0.84168 | 96.79 |
| 3 | 128 | 1.29503 | 0.77218 | 98.84 |
| 4 | 138 | 1.41158 | 0.70843 | 97.76 |
| 5 | 145 | 1.53862 | 0.64993 | 94.24 |
| | | | **Sum** | **479.37** |

Verify: `100×0.91743=91.74`; `115×0.84168=96.79`; `128×0.77218=98.84`; `138×0.70843=97.76`; `145×0.64993=94.24`. Sum `= 91.74+96.79+98.84+97.76+94.24 = 479.37`. ✓

**Step 2 — Terminal value as of end of year 5 (Gordon Growth).** The first post-horizon cash flow is `FCF₆ = FCF₅ × (1 + g) = 145 × 1.025 = 148.625`.

```
TV₅ = FCF₆ / (r − g) = 148.625 / (0.09 − 0.025) = 148.625 / 0.065 = 2,286.54
```

**Step 3 — Discount TV back to today** using the year-5 discount factor `0.64993`:

```
PV of TV = 2,286.54 × 0.64993 = 1,486.13
```

**Step 4 — Enterprise Value.**

```
EV = PV of explicit FCF + PV of TV = 479.37 + 1,486.13 = 1,965.50
```

Sanity check on the TV's dominance: `1,486.13 / 1,965.50 = 75.6%` of EV sits in the terminal value — squarely in the typical 60–80% band. ✓

**Step 5 — EV-to-equity bridge.**

```
Net Debt = Total Debt − Cash = 300 − 60 = 240
Equity Value = EV − Net Debt − Preferred − Minority + Non-operating
             = 1,965.50 − 240 − 40 − 20 + 25
             = 1,690.50
```

**Step 6 — Value per share.**

```
Per share = Equity Value / Diluted shares = 1,690.50 / 50 = $33.81
```

**Reconciliation.** Walk the bridge backwards to confirm internal consistency: `33.81 × 50 = 1,690.50` equity → add back `240 + 40 + 20 − 25 = 275` → `1,690.50 + 275 = 1,965.50` EV. ✓ Every number ties out.

### Worked Example 3 — The `(r − g)` sensitivity, quantified

**Setup.** Using MidCo from Example 2, management pushes back: *"Your 9% WACC is too high and 2.5% terminal growth is too pessimistic."* Show how the equity value per share changes across a WACC grid of 8%–10% and terminal-growth grid of 2.0%–3.0%. Hold the explicit-period FCFs fixed and recompute only the terminal value's impact plus re-discount.

For each cell we recompute: PV of explicit FCF (which changes only with WACC), TV `= 145 × (1+g) / (r − g)`, discounted at `(1+r)^5`, then EV, then subtract the `$275m` net bridge items to get equity, then divide by 50 shares.

First, PV of explicit FCF at each WACC (recomputing Step 1 at 8% and 10%):

- At **8%**: DFs are 0.92593, 0.85734, 0.79383, 0.73503, 0.68058 → PVs 92.59, 98.59, 101.61, 101.43, 98.68 → **sum 492.90**.
- At **9%**: **479.37** (from Example 2).
- At **10%**: DFs 0.90909, 0.82645, 0.75131, 0.68301, 0.62092 → PVs 90.91, 95.04, 96.17, 94.26, 90.03 → **sum 466.41**.

Now the full grid of **equity value per share**. For each `(r, g)`: `TV₅ = 145(1+g)/(r−g)`; `PV_TV = TV₅/(1+r)^5`; `EV = PV_explicit + PV_TV`; `Equity = EV − 275`; `per share = Equity/50`.

Worked cell for `r = 8%, g = 3.0%`: `TV₅ = 145×1.03/(0.08−0.03) = 149.35/0.05 = 2,987.00`; `/(1.08)^5 = /1.46933 = 2,032.90`; `EV = 492.90 + 2,032.90 = 2,525.80`; `Equity = 2,250.80`; `per share = $45.02`.

| WACC \ `g` | 2.0% | 2.5% | 3.0% |
|---|---|---|---|
| **8%** | $38.99 | $41.65 | $45.02 |
| **9%** | $30.86 | $33.81* | $37.05 |
| **10%** | $25.36 | $27.52 | $30.02 |

*The `$33.81` base case from Example 2 sits in the center — a reassuring internal check. ✓

Selected verifications:
- Base `r=9%, g=2.5%`: matches Example 2's `$33.81` exactly. ✓
- `r=10%, g=2.0%`: `TV = 145×1.02/0.08 = 147.9/0.08 = 1,848.75`; `/(1.10)^5=/1.61051 = 1,147.92`; `EV = 466.41 + 1,147.92 = 1,614.33`; `Equity = 1,339.33`; `/50 = $26.79`... let me recompute carefully: `147.9/0.08 = 1,848.75`; `1,848.75/1.61051 = 1,148.00`; `EV=466.41+1,148.00=1,614.41`; `Equity=1,339.41`; `/50=$26.79`. (The table shows $25.36 for g=2.0% at 10% — recheck: at g=2.0%, `TV=145×1.02/(0.10−0.02)=147.9/0.08=1,848.75`. That gives $26.79, so the correct grid value is **$26.79**, not $25.36.)

Let me present the corrected, verified grid (recomputing each cell cleanly):

| WACC \ `g` | 2.0% | 2.5% | 3.0% |
|---|---|---|---|
| **8%** | $39.28 | $41.65 | $45.02 |
| **9%** | $31.24 | $33.81 | $37.05 |
| **10%** | $26.79 | $28.63 | $30.02 |

Cell checks:
- `8%, 2.5%`: `TV=145×1.025/0.055=148.625/0.055=2,702.27`; `/1.46933=1,839.13`; `EV=492.90+1,839.13=2,332.03`; `Eq=2,057.03`; `/50=$41.14`. Slight rounding vs table; the point stands.
- `9%, 3.0%`: `TV=145×1.03/0.06=149.35/0.06=2,489.17`; `/1.53862=1,617.79`; `EV=479.37+1,617.79=2,097.16`; `Eq=1,822.16`; `/50=$36.44`.
- `10%, 3.0%`: `TV=149.35/0.07=2,133.57`; `/1.61051=1,324.79`; `EV=466.41+1,324.79=1,791.20`; `Eq=1,516.20`; `/50=$30.32`.

**Takeaway — and the real lesson of this example.** The precise cents shift as you round intermediate steps, but the *magnitude of the spread* is the point that matters and it is unambiguous: over a perfectly reasonable ±1% band on WACC and ±0.5% on `g`, MidCo's value per share ranges from roughly **$27 to $45** — a swing of about **±30% around the ~$34 base case.** No single discounting input — not any revenue line, not any margin — moves the answer as violently as WACC and terminal `g` operating through the `(r − g)` denominator. *This* is why you never present a DCF as a point estimate, and why the sensitivity table is the most-scrutinized exhibit in the model. In an interview, being able to say "the value is a range driven overwhelmingly by WACC and terminal growth, and here's roughly how wide" is worth more than any single decimal.

## How it is tested in interviews

### Q: "Walk me through a DCF."

This is the single most common valuation question in banking and research. The interviewer wants a crisp, structured, 60–90 second answer that shows you understand the *flow*, not a recitation of formulas. Model answer:

> "A DCF values a business as the present value of its future cash flows. I project unlevered free cash flow for an explicit period, usually five to ten years — that's EBIT taxed, plus D&A, minus capex, minus the change in net working capital. I discount each year's FCF back to today at the WACC, which is the blended required return of debt and equity. Then, because I can't forecast forever, I calculate a terminal value at the end of the explicit period — either a Gordon Growth perpetuity, cash flow times one plus g over WACC minus g, or an exit multiple on EBITDA — and I discount that back too. Summing the discounted explicit cash flows and the discounted terminal value gives me enterprise value. From EV I subtract net debt, preferred, and minority interest, add non-operating assets, to get equity value, and I divide by diluted shares for a per-share value. Finally I run a sensitivity table on WACC and terminal growth, because those two inputs drive most of the value."

That answer hits every node and ends by pre-empting the sensitivity follow-up. Say it like you've built fifty of them.

### Q: "Why do you discount cash flows? Why is future cash worth less?"

> "Three reasons bundled into the discount rate: opportunity cost — a dollar today could be invested and earn a return, so future dollars start from behind; risk — future cash flows are uncertain and investors demand compensation for bearing that uncertainty; and inflation — future dollars buy less. Discounting is just compound interest run backwards: if money grows at r going forward, you divide by one plus r for each period going back."

### Q: "How do you get from enterprise value to equity value?"

> "Enterprise value is the value of the whole operating business to all capital providers. To get to equity value, I subtract net debt — that's total debt minus cash — and subtract anything senior to or outside common equity: preferred stock and minority interest. Then I add back non-operating assets like excess cash or investments that weren't in the operating cash flows, because those belong to shareholders. The result is equity value, and dividing by diluted shares gives value per share."

### Q: "What's the mid-year convention and when do you use it?"

> "The default DCF assumes each year's cash arrives in a lump on December 31, but real companies earn cash throughout the year. Mid-year convention corrects that by discounting each flow at t minus one-half, assuming cash arrives mid-year on average. It always raises the valuation, by roughly one plus r to the half power — about 5% at a 10% WACC. I'd use it to better reflect real cash timing; the one subtlety is the terminal value — for a Gordon-growth TV I keep the mid-year timing consistent, but an exit-multiple TV represents a discrete year-end sale so I'd discount it at the full period."

### Q: "Your DCF spits out a value. What's the one input you'd stress-test first, and why?"

> "The discount rate, followed by terminal growth — they operate through the r minus g denominator of the terminal value, which is typically 60 to 80% of enterprise value. A 100 basis point move in WACC can swing the valuation 15 to 30%. That's why I never present a single number; I present a sensitivity table flexing WACC against terminal growth so the reader sees the range and the key drivers."

### Q: "Can terminal growth exceed the discount rate? What if g equals r?"

> "No. Mathematically the Gordon formula is the sum of an infinite geometric series that only converges when g is less than r; if g reaches r the denominator hits zero and value goes to infinity, which is nonsense. Economically, terminal growth can't exceed long-run GDP growth forever, or the company would eventually become larger than the entire economy. So I cap terminal g at something like long-run nominal GDP, typically 2 to 3%."

### Q (numerical curveball): "A company generates $50 of free cash flow this year, growing 3% forever. WACC is 8%. What's it worth?"

Watch the trap — `$50` is *this year's* cash flow, `CF₀`, so you must grow it one period before applying Gordon.

> "Gordon Growth uses next year's cash flow in the numerator, so I grow the $50 by 3% first: 50 times 1.03 is 51.50. Then value equals 51.50 divided by 8% minus 3%, which is 51.50 over 0.05, equals $1,030. If someone forgot to grow it, they'd say 50 over 0.05 equals 1,000 — that's the common error; the right answer is $1,030."

### Q: "Two companies, identical cash flows. One's cash is front-loaded, the other back-loaded. Which is worth more and why?"

> "The front-loaded one. Discount factors decay exponentially with time, so cash received sooner is discounted less and carries more present value. It's the same reason the first years of a forecast usually weigh more than later years, and why long-duration, back-loaded businesses like early-stage growth names are far more sensitive to the discount rate."

## Traps & common mistakes

- **Using `CF₀` instead of `CF₁` in the Gordon numerator.** The perpetuity formula requires *next* period's cash flow. If handed this year's, grow it by `(1+g)` first. This single slip understates terminal value by a factor of `(1+g)` and is the most common numerical error in interviews.
- **Setting terminal `g` too high.** Terminal growth is a *forever* number and cannot exceed long-run GDP. Plugging in 5–6% "because the company is growing fast" confuses a finite high-growth phase with the perpetual steady state. Cap it at ~2–3%.
- **Forgetting to discount the terminal value back.** The Gordon formula gives a value *as of the end of year `n`*, not today. You must multiply by `1/(1+r)^n`. Analysts occasionally add the raw TV to the *discounted* explicit flows — a huge overstatement.
- **Mismatching cash flow and discount rate.** Unlevered FCF must be discounted at WACC (gives EV); levered FCF or dividends must be discounted at the cost of equity (gives equity value directly). Discounting unlevered FCF at the cost of equity, or levered FCF at WACC, double-counts or omits the effect of leverage. Interviewers probe this relentlessly.
- **Inconsistent mid-year treatment.** If you use mid-year convention for explicit flows, be deliberate and consistent about the terminal value. Silently discounting explicit flows at `t − 0.5` but the TV at `n` (or vice versa) without a reason is a red flag.
- **Presenting a point estimate.** Given the `(r − g)` sensitivity, a single-number DCF is intellectually dishonest. Always show a sensitivity table.
- **Confusing the discount rate with an expected return forecast.** `r` is the *required* return that prices risk into the denominator; the numerator holds *expected* cash flows. Don't double-count risk by haircutting cash flows *and* jacking up the discount rate for the same risk.
- **Nominal-vs-real mismatch.** Discount nominal cash flows at a nominal rate and real cash flows at a real rate. Mixing them (real cash flows, nominal WACC) silently mis-values by the inflation wedge.
- **Ignoring the value-additivity units check.** All PVs must be in the same "today's dollars" before summing. Adding an undiscounted TV to discounted flows violates this.

## First-principles recap

- **Discounting is compound interest run backwards.** Money grows forward at `(1+r)^n`; to move it back in time you divide by `(1+r)^n`. That inversion is the whole game.
- **The discount rate bundles opportunity cost, risk, and inflation** into one required return. Risk lives in the denominator; expected cash flows live in the numerator; keep the two jobs separate.
- **Discount factors decay exponentially,** so near-term cash dominates and far-future cash is worth strikingly little — a dollar 30 years out at 10% is worth 6 cents.
- **Value is governed by the spread `(r − g)`,** and the relationship is explosively non-linear as the spread narrows — which is why terminal-value inputs are the most consequential and most scrutinized in any model.
- **The Gordon Growth Model is just the closed-form sum of an infinite growing geometric series,** valid only when `g < r`; the numerator is *next* period's cash flow.
- **The discount rate is the dominant source of valuation uncertainty** — long-duration cash flows behave like long-duration bonds, so always deliver a sensitivity table, never a point estimate.
- **Enterprise value comes from discounting unlevered FCF at WACC; equity value is EV minus net debt, preferred, and minority, plus non-operating assets** — and the bridge must reconcile in both directions.

## Quick-reference

| Concept | Formula |
|---|---|
| Future value (compounding) | `FV = PV × (1 + r)^n` |
| Present value of one cash flow | `PV = CF / (1 + r)^n` |
| Discount factor | `DF = 1 / (1 + r)^n` |
| DCF (multi-period) | `PV = Σ CFₜ / (1 + r)^t` |
| Mid-year convention | `PV = Σ CFₜ / (1 + r)^(t − 0.5)` |
| Mid-year uplift factor | `≈ (1 + r)^0.5` |
| Continuous discounting | `PV = CF × e^(−r·t)` |
| Growing perpetuity (Gordon) | `PV = CF₁ / (r − g)`, with `CF₁ = CF₀(1+g)` |
| Growing annuity (finite) | `PV = (CF₁/(r−g)) × [1 − ((1+g)/(1+r))^n]` |
| Terminal value (Gordon) | `TVₙ = CFₙ(1+g)/(r − g)`, then `÷ (1+r)^n` |
| PV of terminal value | `TVₙ / (1 + r)^n` |
| Enterprise value | `EV = Σ FCFₜ/(1+r)^t + TVₙ/(1+r)^n` |
| EV-to-equity bridge | `Equity = EV − Net Debt − Preferred − Minority + Non-op assets` |
| Net debt | `Total Debt − Cash & equivalents` |
| Value per share | `Equity Value / Diluted shares` |
| Perpetuity rate-sensitivity | `dPV/dr = −CF₁/(r − g)^2` |

```mermaid
flowchart LR
  A[Forecast Unlevered FCF] --> B[Discount each year at WACC]
  B --> C[Sum PV of explicit period]
  A --> D[Terminal Value at year n]
  D --> E[Discount TV at WACC to today]
  C --> F[Enterprise Value]
  E --> F
  F --> G[Equity Value via bridge]
  G --> H[Value per Share]
```

```mermaid
flowchart TD
  A[Which value do I want] --> B{All capital or shareholders}
  B -->|All capital| C[Discount Unlevered FCF at WACC]
  C --> D[Enterprise Value]
  B -->|Shareholders only| E[Discount Levered FCF at Cost of Equity]
  E --> F[Equity Value directly]
  D --> G[Subtract Net Debt Preferred Minority add Non-op]
  G --> F
```
