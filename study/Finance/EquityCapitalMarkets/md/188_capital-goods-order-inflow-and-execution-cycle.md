# Capital Goods — Order Inflow and the Execution Cycle

## The Problem / Why this matters
Capital goods and engineering companies report an order book, an order inflow and a revenue line, and the relationship between the three determines the earnings trajectory for years. Analysts frequently model revenue as a growth rate on the prior year, which ignores the mechanical constraint that revenue can only come from the book — and misses the fact that this quarter's inflow determines revenue two to three years out.

## Core Idea
Model revenue as **book conversion**, not as a growth rate — opening book plus inflow less execution equals closing book — because the identity forces internal consistency and makes the forecast checkable.

## Why it works this way
An engineering company can only bill what it has been contracted to do. Revenue is therefore a function of the order book and the rate at which it converts, both of which are disclosed or estimable. A growth-rate forecast that implies execution faster than the book supports is arithmetically impossible, and the identity catches it immediately.

```mermaid
graph LR
  A[Opening order book] --> B[+ Order inflow]
  B --> C[- Revenue executed]
  C --> D[+/- Cancellations and adjustments]
  D --> E[Closing order book]
  E --> F[Next period's revenue capacity]
```

## Full technical content

### The three cycles

**1. The ordering cycle** — driven by customer capex decisions, which depend on their own utilisation, financing conditions and confidence. **Leading indicators**: customer capacity utilisation, announced customer capex, government budget allocations for infrastructure and defence, and tender activity on procurement portals.

**2. The execution cycle** — how fast the book converts. Determined by project size, complexity, site readiness, customer approvals and payment. **Longer-cycle orders provide visibility but slow the conversion rate.**

**3. The payment cycle** — milestone-based billing, retention money held until completion, and the gap between work done and cash received. This is where the working-capital intensity of the sector originates.

### The metrics

| Metric | Construction | Reading |
|---|---|---|
| **Order inflow** | New orders won in the period | Leading indicator of revenue in 1–3 years |
| **Book-to-bill** | Inflow ÷ revenue | Above 1 means the book is building |
| **Order book to revenue** | Book ÷ trailing revenue | Years of visibility, read against the execution period |
| **Execution rate** | Revenue ÷ opening book | How fast the book converts; compare to history |
| **Unbilled revenue** | Balance sheet | Work done, not yet invoiced — the early warning |
| **Retention money** | Balance sheet | Cash held by customers until completion |

**Unbilled revenue rising faster than revenue is the sector's clearest warning signal.** It means work has been performed and recognised but not yet billable — because a milestone was not certified, a specification is disputed, or the customer is not ready. It precedes receivable problems and margin disappointments.

### Order book quality — the questions

Per the revenue-visibility chapter, applied specifically:
- **Firm orders or letters of intent?**
- **Is the customer's funding secured** — particularly for private infrastructure and for state-government orders?
- **Fixed price or with escalation clauses?** A fixed-price order in an inflationary period carries the cost risk, which the pass-through chapter frames.
- **What margins were bid?** Orders won in a competitive period appear as revenue years later at those margins.
- **Slow-moving orders** — old orders showing no progress, which are frequently dead but still counted.
- **Concentration** in a few large orders or one customer.

### The margin dynamics

- **Margins are locked at bid**, so today's reported margin reflects the competitive environment of two to three years ago. **A company reporting margin improvement may simply be executing orders won in a tighter market.**
- **Cost overruns** are absorbed by the contractor on fixed-price work.
- **Percentage-of-completion accounting** means revenue and margin depend on estimated total costs, which management revises — and a revision changes previously recognised profit. **Watch for changes in cost estimates disclosed in the notes.**
- **Claims and variations** recognised as revenue before settlement are an aggressive recognition point, and their conversion record is worth checking.

### The cash reality

The sector's defining financial characteristic:
- **Working capital is heavy** — unbilled revenue, receivables, retention money and inventory all consume cash.
- **Cash flow lags profit substantially**, which makes the cumulative CFO versus cumulative PAT check especially important here.
- **Growth consumes cash**, so a rapidly growing order book with strong reported profit and negative operating cash flow is normal in form and dangerous in degree.
- **Retention money** is released only on completion and defect-liability expiry, sometimes years later.

### Building the model

1. **Opening book**, disclosed.
2. **Forecast inflow** from the ordering-cycle indicators, not from a growth assumption.
3. **Apply an execution rate** based on the company's own history and the book's composition.
4. **Compute revenue** as the conversion, and closing book as the residual.
5. **Apply margins by order vintage** where disclosure allows.
6. **Model working capital explicitly** — unbilled, receivables, retention — since it determines the cash outcome and the funding requirement.
7. **Sense-check the implied execution rate** against history; a forecast requiring faster conversion than the company has ever achieved needs a reason.

## Common mistakes
- Modelling revenue as a **growth rate** rather than as book conversion.
- Quoting the **order book** without its quality filters or execution period.
- Missing **unbilled revenue** rising faster than revenue.
- Reading margin improvement as operational when it reflects **older, better-priced orders**.
- Ignoring **changes in estimated project costs**, which restate past profit.
- Treating **claims and variations** recognised as revenue as settled.
- Underestimating **working capital** consumption in a growth phase.
- Forecasting an execution rate the company has never achieved.

## Interview angle
"An engineering company's order book is up 30%. Is that good?" Say revenue can only come from the book, so model it as conversion — opening book plus inflow less execution — rather than as a growth rate, and then interrogate the book's quality: firm orders or letters of intent, whether customer funding is secured, whether pricing is fixed or has escalation clauses, and above all what margins were bid, because today's reported margin reflects the competitive environment of two to three years ago rather than current execution. Then flag the two things that go wrong in this sector: unbilled revenue rising faster than revenue, which means work is recognised but not billable because a milestone was not certified or a specification is disputed, and which precedes receivable and margin problems; and working capital, since unbilled, receivables and retention money all consume cash, so a growing book with strong reported profit and negative operating cash flow is normal in form and needs sizing for degree. Finish with the model check — an implied execution rate faster than the company has ever achieved requires a stated reason.
