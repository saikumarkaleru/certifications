# Chapter 07 — Risk Analysis in Capital Budgeting

## 1. The Problem: The NPV You Computed Is a Comfortable Lie

In Chapter 6 you learned to appraise a project. You forecast the cash flows, picked a discount rate, and computed the Net Present Value. If NPV was positive, you accepted. Clean, decisive, mathematical.

Now sit with an uncomfortable truth. Every one of those cash flows was a **guess about the future**. The ₹40 lakh you wrote down for "Year 3 operating cash flow" is not a fact — it is a hope, dressed up in the false precision of a number with no error bar attached to it.

Consider a real decision. Your company is evaluating a new product line. The finance team hands you this:

| Year | Cash Flow (₹) |
|------|---------------|
| 0 | (10,00,000) |
| 1 | 4,00,000 |
| 2 | 4,00,000 |
| 3 | 5,00,000 |

At a 10% discount rate the NPV comes to roughly ₹+3,25,000. Accept, says the model.

But **where did the ₹4,00,000 for Year 1 come from?** It came from assuming you sell 20,000 units at ₹100 with a ₹80 cost. What if you sell only 15,000 units? What if a competitor launches first and the price falls to ₹90? What if raw material inflation pushes cost to ₹85? Each of those is plausible. Under some combinations the same "accept" project quietly becomes a wealth-destroying trap with a **negative** NPV.

Here is the core problem this chapter solves:

> A single-point NPV tells you the destination if everything goes exactly as forecast. It tells you **nothing** about how likely that is, how far you might miss, or which assumption you most need to protect. Two projects can have identical NPVs — and yet one is a safe bet and the other a coin flip with your factory as the stake.

Capital budgeting decisions are **large, long-lived, and irreversible**. You cannot un-build a plant. The further into the future a cash flow sits, the less you can trust the forecast — yet a ₹10 crore plant is justified precisely by those distant, least-trustworthy years. Ignoring risk does not make a project safe; it only makes you **blind** to the danger you have already accepted.

So the questions this chapter must answer are:

1. **How do we adjust the accept/reject rule itself** so it demands a higher reward from a riskier project? (Risk-adjusted discount rate, certainty equivalent.)
2. **How do we probe a single forecast** to see which assumption is fragile? (Sensitivity analysis.)
3. **How do we model a whole coherent future** rather than one variable at a time? (Scenario analysis.)
4. **How do we attach probabilities** and compute an *expected* NPV, and then measure the *spread* of outcomes around it? (Expected NPV, standard deviation, coefficient of variation.)
5. **How do we handle decisions that unfold in stages**, where later choices depend on earlier outcomes? (Decision trees.)
6. **How do we let a computer roll the dice thousands of times** to see the full shape of what might happen? (Simulation.)

Each technique exists because a simpler one fell short. We will build them in that order.

---

## 2. The Core Idea: A Weather Forecast, Not a Calendar Date

A single-point NPV is like a calendar that says **"It will rain 12 mm on the afternoon of 14 August."** Absurdly precise, and almost certainly wrong in the specifics.

Risk analysis converts that into a **weather forecast**: *"70% chance of rain, most likely 8–15 mm, with a small chance of a washout flood."* Notice what the forecast gives you that the calendar date never could:

- A **central expectation** (what to plan around).
- A **range** (how wrong you might be).
- The **tail risk** (the rare catastrophe you must insure against).
- **What drives it** (the monsoon system, i.e. which variable matters).

That is exactly the upgrade we are performing on capital budgeting. We stop pretending the future is a fixed number and start describing it as a **distribution** — a fan of possibilities, each with a likelihood.

The second analogy, for the discount-rate side of the story: think of the **interest a lender charges**. A bank lends to the Government of India at a low rate, and to a first-time entrepreneur at a much higher rate. Same rupee, different price — because the second borrower **might not pay back**. The extra percentage points are a **risk premium**. When we discount a risky project's cash flows at a higher rate, we are doing precisely what the bank does: demanding more reward per rupee of risk before we part with our capital. Risk isn't just measured; it is **priced into the hurdle**.

Hold both pictures in your head:
- **Weather forecast** = describing the spread of outcomes (sensitivity, scenario, probability, simulation).
- **Risk premium on a loan** = adjusting the decision rule to punish risk (risk-adjusted rate, certainty equivalent).

Everything in this chapter is one of these two moves: **describe the risk**, or **charge for it**.

---

## 3. Why It's Built This Way: Risk vs Uncertainty, and Two Honest Roads

Before the machinery, one distinction the examiner loves and that clarifies your thinking.

**Risk vs Uncertainty (Frank Knight's distinction).**
- **Risk** is when you *can* attach probabilities to outcomes — like a dice throw. You don't know the result, but you know the odds. Insurance companies live here.
- **Uncertainty** is when you *cannot* reliably attach probabilities — a genuinely novel product, an untested market. You know outcomes are possible but not how likely.

In practice, capital budgeting lives in a grey zone: we estimate probabilities from history, judgement, and analysis, knowing they are imperfect. The techniques below span the spectrum — sensitivity analysis needs *no* probabilities (good for true uncertainty), while expected NPV and simulation *require* them (they treat the problem as measurable risk).

**Why two separate roads to adjust the decision rule?**

There are two philosophically different ways to make the accept/reject rule respect risk, and understanding *why both exist* is more important than memorising either.

Road 1 — **Adjust the discount rate (RADR).** Keep the cash flows as forecast, but discount them harder. The logic: risk is a cost, and the cost of risk grows with time, so bake the premium into the rate, where compounding automatically makes it bite harder in later years.

Road 2 — **Adjust the cash flows (Certainty Equivalent, CE).** Shrink each risky cash flow down to the *certain* amount you'd accept in exchange for it, then discount all those "de-risked" flows at the plain **risk-free rate**. The logic: risk and the time value of money are two *different* things, so deal with them *separately* — squeeze the risk out of the numerator first, then apply pure time value in the denominator.

They exist as rivals because each fixes a flaw in the other, and the examiner tests whether you understand the trade-off (Section 4 makes the conflict precise). This is the recurring pattern of the chapter: **no technique is final; each is a response to the limitation of the one before it.**

```mermaid
flowchart TD
    A["Single-point NPV ignores risk"] --> B["How do we make the RULE respect risk"]
    A --> C["How do we DESCRIBE the range of outcomes"]
    B --> D["Adjust the rate<br/>Risk-Adjusted Discount Rate"]
    B --> E["Adjust the cash flows<br/>Certainty Equivalent"]
    C --> F["One variable at a time<br/>Sensitivity Analysis"]
    C --> G["Whole coherent futures<br/>Scenario Analysis"]
    C --> H["Attach probabilities<br/>Expected NPV plus Std Dev"]
    C --> I["Staged decisions<br/>Decision Trees"]
    C --> J["Thousands of trials<br/>Simulation"]
```
*Figure 1: The two families of risk techniques — pricing the risk into the rule, and describing the spread of outcomes.*

---

## 4. Full Technical Content: The Machinery, With the "Why" Attached

### 4.1 Sources of risk — name them before you model them

Cash flows are uncertain because their **components** are uncertain. Listing the drivers is the first analytical act:

- **Project-specific risk** — errors in your own estimates (units, cost, life).
- **Competitive/industry risk** — rivals' actions, technology shifts.
- **Market/economy-wide risk** — inflation, interest rates, GDP cycles, exchange rates.
- **International & political risk** — regulation, taxation, expropriation.

Every technique below is ultimately a way of translating uncertainty in these **inputs** into uncertainty in the **output** (NPV).

### 4.2 Risk-Adjusted Discount Rate (RADR)

**The rule.** Discount the (unchanged) expected cash flows at a rate that includes a risk premium:

$$\text{RADR} = R_f + \text{Risk Premium}$$

where $R_f$ is the risk-free rate. Then apply the ordinary NPV formula:

$$\text{NPV} = \sum_{t=1}^{n} \frac{CF_t}{(1 + \text{RADR})^{t}} - CF_0$$

**Why it works.** A higher denominator shrinks present values. Riskier project → higher premium → higher hurdle → project must produce more to survive. Because the rate is *compounded*, $(1+r)^t$, the penalty **grows automatically with time** — distant cash flows (the least trustworthy) get punished the most. That is elegant and intuitive.

**The hidden flaw — and why CE was invented.** That same compounding is a **crude assumption**: RADR forces risk to increase at a constant compound rate every year. But not every project's risk grows smoothly with time. A project might be very risky in Year 1 (will the product even launch?) and *safer* later once it's established. RADR cannot express that shape — it mechanically assumes risk keeps compounding. This over-penalises long, back-loaded projects. That flaw is precisely what the Certainty Equivalent method fixes.

### 4.3 Certainty Equivalent (CE) approach

**The rule.** Convert each risky cash flow into its **certainty equivalent** by multiplying by a certainty-equivalent coefficient $\alpha_t$ (alpha), then discount those certain amounts at the **risk-free rate**:

$$\text{NPV} = \sum_{t=1}^{n} \frac{\alpha_t \times CF_t}{(1 + R_f)^{t}} - CF_0$$

The coefficient is defined as:

$$\alpha_t = \frac{\text{Certain cash flow the decision-maker would accept}}{\text{Expected risky cash flow}}$$

$\alpha_t$ lies between 0 and 1. **Lower $\alpha$ = more risk** (you'd swap the risky flow for a much smaller sure thing). As risk perception rises, $\alpha$ falls.

**Why it's the theoretically superior method.** It separates the **two things RADR tangles together**:
- Time value → handled *purely* by discounting at $R_f$.
- Risk → handled *separately and explicitly* in the numerator, year by year.

Because each year gets its **own** $\alpha_t$, the analyst can say "Year 1 is very risky ($\alpha_1 = 0.9$... wait, low alpha means risky, so $\alpha_1 = 0.7$), Year 5 is safer once established ($\alpha_5 = 0.85$)" — a flexibility RADR simply does not have. Theory prefers CE for this honesty.

**Why RADR still dominates in practice.** Estimating a defensible $\alpha_t$ for every single year is subjective and hard to justify to a board. A single risk-adjusted rate is easier to communicate, benchmark, and defend. So CE wins the argument but RADR wins the meeting.

**The reconciliation (exam favourite).** The two methods give the *same* NPV when their implied risk treatments agree. The relationship between the coefficient and the rates is:

$$\alpha_t = \frac{(1 + R_f)^{t}}{(1 + \text{RADR})^{t}}$$

Because RADR > $R_f$, the denominator grows faster, so $\alpha_t$ **declines as $t$ rises** — meaning RADR *implicitly* assumes risk keeps growing every year. This equation is the mathematical proof of RADR's hidden assumption from Section 4.2.

| Feature | RADR | Certainty Equivalent |
|---|---|---|
| What is adjusted | The discount rate (denominator) | The cash flows (numerator) |
| Discount rate used | Risk-free + premium | Risk-free rate only |
| Risk each year | Forced to grow at compound rate | Set independently per year |
| Ease of use | Easy, board-friendly | Harder, subjective per year |
| Theoretical soundness | Weaker (mixes risk and time) | Stronger (separates them) |

### 4.4 Sensitivity Analysis — "what breaks this project?"

RADR and CE change the *rule*. But they don't tell you **which assumption is dangerous**. Sensitivity analysis does.

**The idea.** Take one input at a time, flex it up or down (say ±10%), hold everything else constant, and watch what happens to NPV. The input that moves NPV the most is the **most sensitive** — that's where your forecasting effort and managerial vigilance must concentrate.

**Two ways to express it in the exam:**
1. **NPV sensitivity** — recompute NPV for a given % change in each variable; the largest swing = most critical.
2. **Break-even / margin of safety** — find the % change in each variable that drives NPV to **zero**. The variable needing the *smallest* adverse change to wipe out NPV is the most critical (thinnest safety margin).

$$\text{Sensitivity margin (\%)} = \frac{\text{NPV}}{\text{PV of the variable being flexed}} \times 100$$

**Why it's powerful and where it fails.** It needs **no probabilities** — perfect for genuine uncertainty. It's transparent and pinpoints the variable to defend. **But** it flexes variables *one at a time* and in *isolation*, which is unrealistic — in a recession, sales volume *and* price *and* cost all move together. It tells you *what* is sensitive, not *how likely* the adverse move is. Those two gaps are exactly why scenario analysis and probability analysis come next.

### 4.5 Scenario Analysis — flex everything together, coherently

**The idea.** Instead of one variable at a time, define a small number of **internally consistent complete states of the world** — typically Pessimistic, Most Likely, Optimistic — where *every* variable is set to the value appropriate to that world simultaneously. Compute NPV for each.

**Why it beats sensitivity.** In a "recession" scenario, volume falls *and* price falls *and* costs may rise — sensitivity analysis would never capture that *joint* movement. Scenario analysis respects the fact that variables are **correlated**. Assigning rough probabilities to the three scenarios lets you compute an expected NPV across them.

**Its limit.** Only a handful of scenarios — reality has infinitely many. That gap is what simulation fills.

### 4.6 Probability, Expected NPV, and measuring spread

Now we attach **probabilities** to outcomes and compute genuine statistical measures. This is the heart of quantitative risk analysis.

**Expected value of a cash flow:**

$$\overline{CF_t} = \sum_{i=1}^{m} p_i \times CF_{ti}$$

where $p_i$ is the probability of outcome $i$ (probabilities sum to 1). This is the **probability-weighted average** — the centre of the fan.

**Expected NPV:**

$$\overline{\text{NPV}} = \sum_{t=1}^{n} \frac{\overline{CF_t}}{(1+r)^{t}} - CF_0$$

**Standard Deviation — measuring the spread.** Expected NPV is only the centre. Two projects with the *same* expected NPV can have wildly different **dispersion**. Standard deviation ($\sigma$) measures how far outcomes scatter around the mean:

$$\sigma = \sqrt{\sum_{i=1}^{m} p_i \left(CF_i - \overline{CF}\right)^{2}}$$

A **higher $\sigma$ = more risk** (wider fan of outcomes). $\sigma$ is an *absolute* measure of risk in rupees.

**Coefficient of Variation — risk per rupee of return.** Here's the trap $\sigma$ falls into: a big project naturally has a big $\sigma$ just because the numbers are big, not because it's riskier *per rupee*. To compare projects of **different sizes**, we standardise:

$$\text{CV} = \frac{\sigma}{\overline{\text{NPV}} \text{ (or expected value)}}$$

CV is **risk per unit of return**. When two projects differ in scale or in expected return, **CV is the correct comparator, not $\sigma$.** *Lower CV = better risk-return trade-off.* This distinction (when to use $\sigma$ vs CV) is a classic exam discriminator.

**Independent vs dependent cash flows.** If each year's cash flow is **independent**, the standard deviation of the *NPV* is:

$$\sigma_{\text{NPV}} = \sqrt{\sum_{t=1}^{n} \frac{\sigma_t^{2}}{(1+r)^{2t}}}$$

If cash flows are **perfectly correlated** (a bad year stays bad), risk is higher:

$$\sigma_{\text{NPV}} = \sum_{t=1}^{n} \frac{\sigma_t}{(1+r)^{t}}$$

Perfect correlation gives a larger $\sigma$ than independence — because there's no year-to-year averaging to smooth the shocks. Knowing *which* formula to apply from the wording ("independent" vs "correlated") is itself an examiner trick.

### 4.7 Decision Trees — when today's choice depends on tomorrow's outcome

Everything so far assumes a **single, once-and-for-all** decision. But many real investments are **sequential**: build a pilot plant now, and *only if* it succeeds, invest in the full plant. The second decision depends on the first outcome. A flat expected-NPV calculation can't represent that branching.

**The idea.** Draw the decision as a **tree**:
- **Decision nodes** (squares) — points where *you* choose.
- **Chance/outcome nodes** (circles) — points where *nature* decides, each branch carrying a probability.
- **Branches** — the flows.

**Roll back (fold back) the tree.** Evaluate from **right to left**: at each chance node compute the expected value; at each decision node pick the branch with the highest value. The initial decision's value is the expected value of playing optimally throughout.

**Why it matters.** It captures the *value of flexibility* — the option to abandon, expand, or wait. A rigid NPV ignores that you can *react* to how things unfold; a decision tree rewards the fact that you'll make good choices later.

```mermaid
flowchart LR
    D1["Decision<br/>Launch pilot or not"] --> C1(("Chance<br/>Pilot result"))
    C1 -->|"Success p=0.6"| D2["Decision<br/>Build full plant"]
    C1 -->|"Failure p=0.4"| E1["Stop<br/>Small loss"]
    D2 -->|"Expand"| C2(("Chance<br/>Market demand"))
    D2 -->|"Abandon"| E2["Recover salvage"]
    C2 -->|"High p=0.7"| E3["Large gain"]
    C2 -->|"Low p=0.3"| E4["Modest gain"]
```
*Figure 2: A two-stage decision tree — squares are choices you control, circles are outcomes nature controls; you fold back from right to left.*

### 4.8 Simulation — let the computer live a thousand futures

Scenario analysis gives three futures; reality has millions. **Monte Carlo simulation** (Hertz's technique, 1964) is the industrial-scale answer.

**The idea.** For *every* uncertain input (units, price, cost, life, salvage), specify a **probability distribution** rather than a single number. Then the computer:
1. Randomly draws one value from each input's distribution.
2. Computes the NPV for that one complete random future.
3. Repeats thousands of times.
4. Plots the **distribution of NPVs** that results.

**What you get that nothing else provides.** Not one NPV, not three — a **full probability distribution of NPV**: the mean, the standard deviation, and crucially the **probability that NPV < 0** (the chance the project destroys value). It handles many variables *and* their correlations at once.

**The catch.** It is data-hungry and model-dependent — you must specify every distribution and every correlation, and a wrong distribution in gives garbage out. It's expensive and can create false confidence. But conceptually it is the natural end-point: scenario analysis with the number of scenarios turned up to infinity.

```mermaid
flowchart TD
    A["Define distribution for each input<br/>units price cost life salvage"] --> B["Randomly sample one value per input"]
    B --> C["Compute NPV for this trial"]
    C --> D{"Enough trials"}
    D -->|"No"| B
    D -->|"Yes"| E["Plot distribution of NPV"]
    E --> F["Read mean std dev and probability NPV below zero"]
```
*Figure 3: The Monte Carlo simulation loop — repeat the draw-and-compute cycle thousands of times to build the NPV distribution.*

---

## 5. Worked Examples

### Example 1 — Sensitivity Analysis (which assumption breaks the project?)

**Data.** A project needs an initial outlay of ₹10,00,000 and lasts 4 years. Expected figures per year:

- Annual sales volume: 10,000 units
- Selling price: ₹60 per unit
- Variable cost: ₹35 per unit
- Annual fixed cost (cash): ₹80,000
- Cost of capital: 10%; ignore tax; no salvage.

**Base-case NPV.**

Contribution per unit = 60 − 35 = ₹25.
Annual cash flow = (10,000 × 25) − 80,000 = 2,50,000 − 80,000 = **₹1,70,000**.

PV factor of annuity, 10%, 4 years = 3.1699.

PV of inflows = 1,70,000 × 3.1699 = ₹5,38,883.
NPV = 5,38,883 − 10,00,000 = **₹(4,61,117)**.

Hold on — the base case is **negative**. Let me re-scale so the illustration is instructive. Revise annual volume to **25,000 units** (the rest unchanged).

Annual cash flow = (25,000 × 25) − 80,000 = 6,25,000 − 80,000 = **₹5,45,000**.
PV of inflows = 5,45,000 × 3.1699 = ₹17,27,596.
**Base NPV = 17,27,596 − 10,00,000 = ₹7,27,596.** Positive — accept on base case.

**Now flex each variable by an adverse 10%, one at a time.**

*(a) Selling price −10%:* price 60 → 54. Contribution 54 − 35 = 19.
CF = (25,000 × 19) − 80,000 = 4,75,000 − 80,000 = 3,95,000.
PV inflows = 3,95,000 × 3.1699 = 12,52,111. NPV = **₹2,52,111**.
NPV fell from 7,27,596 → 2,52,111, a drop of ₹4,75,485 (a **65%** fall).

*(b) Variable cost +10%:* cost 35 → 38.5. Contribution 60 − 38.5 = 21.5.
CF = (25,000 × 21.5) − 80,000 = 5,37,500 − 80,000 = 4,57,500.
PV inflows = 4,57,500 × 3.1699 = 14,50,229. NPV = **₹4,50,229**.
Drop of ₹2,77,367 (a **38%** fall).

*(c) Volume −10%:* 25,000 → 22,500.
CF = (22,500 × 25) − 80,000 = 5,62,500 − 80,000 = 4,82,500.
PV inflows = 4,82,500 × 3.1699 = 15,29,477. NPV = **₹5,29,477**.
Drop of ₹1,98,119 (a **27%** fall).

*(d) Initial outlay +10%:* 10,00,000 → 11,00,000.
NPV = 17,27,596 − 11,00,000 = **₹6,27,596**.
Drop of ₹1,00,000 (a **14%** fall).

**Sensitivity ranking (most to least critical):**

| Variable flexed −/+10% | New NPV (₹) | Fall in NPV (₹) | % Fall | Rank |
|---|---|---|---|---|
| Selling price | 2,52,111 | 4,75,485 | 65% | **1 (most critical)** |
| Variable cost | 4,50,229 | 2,77,367 | 38% | 2 |
| Sales volume | 5,29,477 | 1,98,119 | 27% | 3 |
| Initial outlay | 6,27,596 | 1,00,000 | 14% | 4 (least critical) |

**Interpretation.** NPV is **most sensitive to selling price** — a mere 10% price slip cuts NPV by nearly two-thirds. Management should protect pricing (contracts, brand, differentiation) above all else, and forecast price with the most care. Note the *insight*: price hits hardest because it changes contribution *without* any offset, whereas the outlay is a one-time, undiscounted-into-the-future hit.

**Break-even margin check (variable = selling price).** How far can price fall before NPV = 0? NPV = 0 needs PV inflows = 10,00,000, i.e. annual CF = 10,00,000 / 3.1699 = ₹3,15,467. Required contribution = (3,15,467 + 80,000)/25,000 = ₹15.82 per unit → price = 35 + 15.82 = ₹50.82. That's a fall of (60 − 50.82)/60 = **15.3%**. The price has only a ~15% safety margin — the thinnest of all variables, confirming it as the critical driver.

### Example 2 — Expected NPV, Standard Deviation & Coefficient of Variation

**Data.** Two mutually exclusive projects, each costing ₹1,00,000, single year life, cost of capital 10%. Year-1 cash flows depend on the economy:

| State | Probability | Project A CF (₹) | Project B CF (₹) |
|---|---|---|---|
| Recession | 0.30 | 90,000 | 40,000 |
| Normal | 0.40 | 1,20,000 | 1,20,000 |
| Boom | 0.30 | 1,50,000 | 2,00,000 |

**Step 1 — Expected cash flow.**

Project A: (0.30 × 90,000) + (0.40 × 1,20,000) + (0.30 × 1,50,000)
= 27,000 + 48,000 + 45,000 = **₹1,20,000**.

Project B: (0.30 × 40,000) + (0.40 × 1,20,000) + (0.30 × 2,00,000)
= 12,000 + 48,000 + 60,000 = **₹1,20,000**.

**Identical expected cash flow.** A naive analyst would call them equal. They are not.

**Step 2 — Expected NPV.**

Discount factor at 10%, 1 year = 0.9091.
Both: Expected NPV = (1,20,000 × 0.9091) − 1,00,000 = 1,09,091 − 1,00,000 = **₹9,091**. Same for both.

**Step 3 — Standard deviation of the cash flow.**

*Project A:*

| State | p | CF − mean | (CF−mean)² | p × (CF−mean)² |
|---|---|---|---|---|
| Recession | 0.30 | −30,000 | 90,00,00,000 | 27,00,00,000 |
| Normal | 0.40 | 0 | 0 | 0 |
| Boom | 0.30 | +30,000 | 90,00,00,000 | 27,00,00,000 |

Variance = 54,00,00,000. $\sigma_A = \sqrt{54,00,00,000}$ = **₹23,238**.

*Project B:*

| State | p | CF − mean | (CF−mean)² | p × (CF−mean)² |
|---|---|---|---|---|
| Recession | 0.30 | −80,000 | 6,40,00,00,000 | 1,92,00,00,000 |
| Normal | 0.40 | 0 | 0 | 0 |
| Boom | 0.30 | +80,000 | 6,40,00,00,000 | 1,92,00,00,000 |

Variance = 3,84,00,00,000. $\sigma_B = \sqrt{3,84,00,00,000}$ = **₹61,968**.

**Step 4 — Interpret.** Same expected NPV (₹9,091), but Project B's spread ($\sigma$ = ₹61,968) is nearly **three times** Project A's (₹23,238). Project B is far riskier — its recession outcome (₹40,000) doesn't even cover the outlay, so its NPV in recession is negative.

**Step 5 — Coefficient of variation** (here both have equal expected value, so ranking by $\sigma$ already suffices, but compute CV on the cash flow for completeness):

CV_A = 23,238 / 1,20,000 = **0.194**.
CV_B = 61,968 / 1,20,000 = **0.516**.

**Decision.** For a **risk-averse** decision-maker, choose **Project A** — same expected reward, much lower risk (lower $\sigma$ and lower CV). This example makes the chapter's central point concrete: *expected NPV alone is not enough; you must look at dispersion.*

**When would CV (not $\sigma$) be the decider?** If the two projects had *different* expected NPVs — say B also had a higher expected return — then comparing raw $\sigma$ would be unfair to the bigger project. CV normalises risk per rupee of return and becomes the correct tie-breaker.

### Example 3 — Certainty Equivalent vs RADR (and their reconciliation)

**Data.** Project outlay ₹6,00,000. Expected (risky) cash flows and management's certainty-equivalent coefficients:

| Year | Expected CF (₹) | CE coefficient αₜ |
|---|---|---|
| 1 | 3,00,000 | 0.90 |
| 2 | 3,00,000 | 0.80 |
| 3 | 3,00,000 | 0.70 |

Risk-free rate = 6%. Company's risk-adjusted rate = 12%.

**Part A — CE method (discount certain amounts at 6%).**

| Year | CF | αₜ | Certain CF (₹) | PVF @6% | PV (₹) |
|---|---|---|---|---|---|
| 1 | 3,00,000 | 0.90 | 2,70,000 | 0.9434 | 2,54,718 |
| 2 | 3,00,000 | 0.80 | 2,40,000 | 0.8900 | 2,13,600 |
| 3 | 3,00,000 | 0.70 | 2,10,000 | 0.8396 | 1,76,316 |

PV of inflows = 2,54,718 + 2,13,600 + 1,76,316 = ₹6,44,634.
**NPV (CE) = 6,44,634 − 6,00,000 = ₹44,634.** Accept.

**Part B — RADR method (discount full CF at 12%).**

| Year | CF (₹) | PVF @12% | PV (₹) |
|---|---|---|---|
| 1 | 3,00,000 | 0.8929 | 2,67,870 |
| 2 | 3,00,000 | 0.7972 | 2,39,160 |
| 3 | 3,00,000 | 0.7118 | 2,13,540 |

PV of inflows = 7,20,570. **NPV (RADR) = 7,20,570 − 6,00,000 = ₹1,20,570.** Accept.

**Why do they differ so much (₹44,634 vs ₹1,20,570)?** Because the two methods embed *different* risk assumptions. The CE coefficients here (0.90, 0.80, 0.70) penalise risk **harder** than the 12% RADR does. We can prove this by backing out the RADR's *implied* CE coefficients using $\alpha_t = (1.06/1.12)^t$:

| Year | Implied αₜ from RADR = (1.06/1.12)ᵗ |
|---|---|
| 1 | 0.9464 |
| 2 | 0.8957 |
| 3 | 0.8478 |

The RADR *implicitly* assumes gentler coefficients (0.946, 0.896, 0.848) than management's stated (0.90, 0.80, 0.70). Management is **more cautious** than the 12% rate reflects, so the CE NPV is lower. **Lesson:** the two methods reconcile *only* when the stated $\alpha_t$ equals the RADR-implied $\alpha_t$. They are the same machine viewed from two ends — and the divergence here is a diagnostic, not an error.

### Example 4 — Decision Tree (staged investment with the option to abandon)

**Data.** A firm can run a market test for ₹1,00,000 now. Test outcomes: **Favourable** (p = 0.6) or **Unfavourable** (p = 0.4). If favourable, it may invest ₹5,00,000 in full production, whose *present value of future cash flows* (already discounted) is either ₹12,00,000 (p = 0.7) or ₹4,00,000 (p = 0.3). If unfavourable, full production's PV would be ₹6,00,000 (p = 0.5) or ₹2,00,000 (p = 0.5). The firm will invest only where it pays; otherwise it walks away (₹0 further). Ignore discounting of the ₹5,00,000 and test cost for simplicity.

**Fold back from the right.**

*Favourable branch — value if it invests:*
Expected PV of production = (0.7 × 12,00,000) + (0.3 × 4,00,000) = 8,40,000 + 1,20,000 = ₹9,60,000.
Net of ₹5,00,000 investment = 9,60,000 − 5,00,000 = **₹4,60,000** (positive → invest). Value at this decision node = ₹4,60,000.

*Unfavourable branch — value if it invests:*
Expected PV = (0.5 × 6,00,000) + (0.5 × 2,00,000) = 3,00,000 + 1,00,000 = ₹4,00,000.
Net of ₹5,00,000 = 4,00,000 − 5,00,000 = **₹(1,00,000)** (negative → do NOT invest). Value at this node = **₹0** (abandon).

*Roll back to the test-result chance node:*
Expected value = (0.6 × 4,60,000) + (0.4 × 0) = ₹2,76,000.

*Initial decision — run the test?*
Value = 2,76,000 − 1,00,000 (test cost) = **₹1,76,000 > 0 → run the test.**

**The insight the tree reveals.** The *option to abandon* after an unfavourable test is worth real money. If the firm had committed to full production regardless, the unfavourable branch would have dragged expected value down by (0.4 × −1,00,000) = −40,000. By retaining the *right but not the obligation* to proceed, it protects that downside. A flat NPV cannot see this flexibility; the decision tree prices it.

---

## 6. Framework Summary & Presentation Format

For a **written exam answer**, present risk analysis in this disciplined order (examiners reward structure):

1. **State the base-case NPV** and note it ignores risk.
2. **Identify the technique demanded** by the question wording (see cue table below).
3. **Show the working in a table** — expected values, deviations, PV factors, all visible.
4. **Compute the risk measure** ($\sigma$, CV, expected NPV, tree roll-back).
5. **Interpret and decide** — never stop at a number; state the accept/reject and *why*, referencing risk appetite.

**Question-cue → technique map:**

| The question says... | Use this technique |
|---|---|
| "how much does NPV change if price falls X%" | Sensitivity analysis |
| "best / worst / most-likely case" | Scenario analysis |
| "probabilities of cash flows... expected NPV" | Expected NPV |
| "which project is riskier" (same size/return) | Standard deviation |
| "which project is riskier" (different size/return) | Coefficient of variation |
| "risk-adjusted rate" / "premium over risk-free" | RADR |
| "certainty equivalent coefficients / factors" | CE method |
| "test market then decide / sequential / abandon option" | Decision tree |
| "distribution of every input / thousands of trials" | Simulation |

```mermaid
flowchart TD
    Q["What does the question give you"] --> A{"Probabilities provided"}
    A -->|"No"| B{"One variable or whole states"}
    B -->|"One at a time"| C["Sensitivity Analysis"]
    B -->|"Whole states"| D["Scenario Analysis"]
    A -->|"Yes"| E{"Single stage or sequential"}
    E -->|"Single stage"| F["Expected NPV then Std Dev and CV"]
    E -->|"Sequential with later choices"| G["Decision Tree fold back"]
    Q --> H{"Adjust the decision rule"}
    H -->|"Adjust rate"| I["RADR"]
    H -->|"Adjust cash flows"| J["Certainty Equivalent"]
```
*Figure 4: A decision map for selecting the correct risk technique from the wording of an exam problem.*

---

## 7. Connections

- **Chapter 6 (Investment Decisions).** This chapter is a *direct extension* of NPV. Every risk method still ends in an NPV or a modified NPV; you are upgrading the *inputs* (cash flows via CE, scenarios, probabilities) or the *rate* (RADR), not replacing the appraisal engine.
- **Cost of Capital.** The risk-free rate $R_f$ and the risk premium in RADR come straight from cost-of-capital theory. The **CAPM** ($R_f + \beta(R_m - R_f)$) is the market-based way to *derive* a project's risk-adjusted rate — RADR and CAPM shake hands here.
- **Portfolio theory & diversification.** Standard deviation and coefficient of variation are the same tools used to measure security and portfolio risk. Correlation between projects' cash flows echoes correlation between securities — a firm's projects form a *portfolio*, and diversification can reduce total $\sigma$.
- **Leverage & Break-even (Chapter on Leverage).** Sensitivity analysis's break-even margin is conceptually the operating break-even point: high fixed cost (operating leverage) makes NPV *more* sensitive to volume — a direct link between cost structure and project risk.
- **Strategic Management (SM side).** Scenario analysis and decision trees map onto **strategic option analysis** and staged/real-option thinking — the "flexibility" a decision tree prices is the same *strategic flexibility* SM prizes.

---

## 8. Traps & Examiner Tricks

1. **Confusing $\sigma$ with CV.** Same expected value → rank by $\sigma$. *Different* expected values or project sizes → **must** use CV. Ranking big projects by raw $\sigma$ is the single most common error.
2. **Wrong $\sigma_{NPV}$ formula.** "Independent cash flows" → use the square-root-of-sum-of-squares formula (discount by $(1+r)^{2t}$). "Perfectly correlated" → simple sum of discounted $\sigma_t$. Read the wording; they give different answers.
3. **CE discount rate.** In the certainty-equivalent method, discount at the **risk-free rate**, *never* the risk-adjusted rate. Using RADR on already-de-risked flows **double-counts** risk. Losing a mark here is pure carelessness.
4. **RADR direction.** Higher risk → *higher* rate → *lower* NPV. Some students mistakenly *lower* the rate for risk. The premium is *added*.
5. **$\alpha$ direction.** Lower certainty-equivalent coefficient = *more* risk. $\alpha$ falls as risk rises and (in RADR-implied form) falls as the year gets later.
6. **Sensitivity = "which is most critical", not "which is good".** The most sensitive variable is the *most dangerous* to mis-estimate — the one to control — not necessarily the biggest contributor to NPV.
7. **Decision tree fold-back direction.** Always evaluate **right to left**. At *chance* nodes take expected values; at *decision* nodes take the *maximum*. Averaging at a decision node (instead of choosing the best) is wrong — you *control* that node.
8. **Forgetting the abandonment option value.** In staged problems, a negative continuation branch is replaced by **₹0 (walk away)**, not the negative number — you won't invest in a value-destroying stage.
9. **Probabilities must sum to 1.** A quick sanity check; if a question's probabilities don't sum to 1, re-read (often conditional probabilities that need multiplying along the branch).
10. **Expected NPV ≠ any actual outcome.** The expected NPV (e.g. ₹9,091) may be a value that *never actually occurs* in any single state. It's a long-run average, not a prediction of one play.

---

## 9. First-Principles Recap

Strip everything away and here is the logic, rebuilt from nothing:

1. A forecast cash flow is a **guess**, so a single NPV is a point estimate with an invisible error bar. Pretending the bar isn't there doesn't remove the risk — it removes your *awareness* of it.
2. There are only **two honest responses** to that: change the **decision rule** so it charges for risk, or **describe** the range of outcomes so you can judge them.
3. **Charging for risk** can be done in the **rate** (RADR — easy, but forces risk to compound with time) or in the **cash flows** (Certainty Equivalent — theoretically cleaner, separates risk from time, but subjective). They are the same machine from two ends and reconcile via $\alpha_t = (1.06/1.12)^t$-type relations.
4. **Describing risk** escalates in sophistication as each method's limits appear: **sensitivity** (one variable, no probabilities) → **scenario** (coherent whole states) → **expected NPV + $\sigma$ + CV** (probabilities and spread) → **decision trees** (staged, flexible choices) → **simulation** (every input as a distribution, infinite scenarios).
5. The **centre** of the outcome fan is expected NPV; the **width** is standard deviation; the **width per rupee of return** is the coefficient of variation. A rational decision weighs *both* centre and width against your **risk appetite**.
6. Ultimately, risk analysis doesn't give you certainty — nothing can. It gives you an **informed relationship with uncertainty**: you know your central bet, how wrong you might be, which assumption to guard, and what the disaster case costs. That is the entire point.

---

## 10. Quick-Revision Sheet

**Core formulas**

| Concept | Formula |
|---|---|
| RADR | $R_f$ + Risk premium; NPV = Σ CFₜ/(1+RADR)ᵗ − CF₀ |
| Certainty Equivalent | NPV = Σ (αₜ·CFₜ)/(1+R_f)ᵗ − CF₀ |
| CE coefficient | αₜ = Certain CF / Expected risky CF (0 ≤ α ≤ 1) |
| CE–RADR reconciliation | αₜ = (1+R_f)ᵗ / (1+RADR)ᵗ |
| Expected cash flow | $\overline{CF}$ = Σ pᵢ·CFᵢ |
| Expected NPV | Σ $\overline{CF_t}$/(1+r)ᵗ − CF₀ |
| Standard deviation | σ = √[Σ pᵢ(CFᵢ − $\overline{CF}$)²] |
| Coefficient of variation | CV = σ / Expected value |
| σ of NPV (independent) | √[Σ σₜ²/(1+r)²ᵗ] |
| σ of NPV (perfectly correlated) | Σ σₜ/(1+r)ᵗ |
| Sensitivity margin | NPV / PV of the variable × 100 |

**Decision rules at a glance**

- **RADR:** higher risk → higher rate → lower NPV. Accept if NPV > 0.
- **CE:** de-risk flows with αₜ, discount at **risk-free** rate. Accept if NPV > 0.
- **Sensitivity:** variable with the **biggest NPV swing** / **thinnest margin** = most critical → guard it.
- **Scenario:** compute NPV in pessimistic / likely / optimistic; probability-weight if asked.
- **Expected NPV + risk:** same size/return → pick **lower σ**; different size/return → pick **lower CV**.
- **Decision tree:** fold back right→left; expected value at circles, maximum at squares; replace negative continuation with **₹0 (abandon)**.
- **Simulation:** distribution per input → thousands of trials → read mean, σ, and **P(NPV < 0)**.

**Risk vs uncertainty:** Risk = probabilities knowable (expected NPV, simulation apply). Uncertainty = probabilities unknowable (sensitivity, scenario apply — they need no probabilities).

**One-line memory hooks**
- *RADR punishes the rate; CE punishes the cash flow.*
- *σ is risk in rupees; CV is risk per rupee.*
- *Sensitivity finds the fragile assumption; scenario moves them all together; simulation moves them all, forever.*
- *A decision tree pays you for the right to change your mind.*
