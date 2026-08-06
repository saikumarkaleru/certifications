# Margin Bridge Analysis

## The Problem / Why this matters
"EBITDA margin fell 220bp" is a fact, not an analysis. Whether it matters depends entirely on what caused it — a mix shift toward a lower-margin but higher-return segment is a different event from pricing pressure, which is different again from a temporary input cost spike or from operating deleverage on a volume miss. A margin bridge decomposes the change into its drivers, and building one is what converts a reported number into a view.

## Core Idea
Decompose every margin change into **volume, price, mix, input cost, and fixed-cost absorption** — because each has a different persistence and a different implication for the forecast.

## Why it works this way
Margin is an output of several independent variables that can move in opposite directions and cancel. A 220bp decline can conceal 150bp of pricing gains offset by 370bp of cost inflation, which is a completely different situation from a uniform 220bp deterioration — and the forecast implications diverge entirely.

```mermaid
graph LR
  A[Opening margin] --> B[+/- Price realisation]
  B --> C[+/- Input cost]
  C --> D[+/- Product/customer mix]
  D --> E[+/- Fixed-cost absorption on volume]
  E --> F[+/- One-offs]
  F --> G[Closing margin]
```

## Full technical content

### The components

| Driver | How to isolate it | Persistence |
|---|---|---|
| **Price/realisation** | Change in revenue per unit at constant mix | Persistent until competitive response |
| **Input cost** | Change in cost per unit of key inputs | Cyclical; reverses |
| **Mix** | Shift in the revenue share of segments with different margins | Persistent if structural |
| **Operating leverage** | Fixed cost per unit change from volume | Reverses with volume |
| **Cost efficiency** | Change in variable cost per unit at constant input prices | Persistent if genuine |
| **One-offs** | Identified separately | Not persistent by definition |

### Building the bridge

The practical method, requiring only disclosed data in most sectors:

1. **Start with the prior-period margin.**
2. **Price effect** = (current realisation − prior realisation) × current volume, expressed as a margin impact.
3. **Input cost effect** = (current input cost per unit − prior) × current volume.
4. **Mix effect** = the change explained by the shift in revenue weights across segments at constant segment margins.
5. **Operating leverage effect** = change in fixed cost per unit × volume, which follows directly from the fixed-cost base and the volume change.
6. **Residual** = efficiency and anything unexplained. **A large residual means the bridge is incomplete**, and chasing it down is where the useful discoveries happen.
7. **Reconcile to the reported margin.**

**Where segment disclosure is limited**, build the bridge at the level the data supports and say so. A partial bridge with stated limitations beats no bridge.

### Reading the result

- **Price-driven decline** — the most serious, since it indicates competitive pressure or lost pricing power, and it does not self-correct.
- **Input-cost-driven decline** — cyclical; recovery depends on the pass-through record, per the pass-through chapter.
- **Mix-driven decline** — check whether the lower-margin business earns adequate *returns*. **A lower-margin, low-capital business can earn a higher RoCE than the high-margin one it displaced**, in which case a falling margin is good news badly presented.
- **Operating-leverage decline** — arithmetic, reverses when volume recovers, and should not be read as deterioration.
- **Efficiency-driven gains** — genuine and persistent, but verify they are not deferred maintenance or cut advertising, which is borrowing margin from later periods.

### The mix point, extended

Mix deserves emphasis because it is the most misread:
- **Segment mix** — a higher share of a structurally lower-margin division.
- **Product mix** — premium versus mass, which usually moves margin the other way.
- **Customer mix** — large customers negotiate better terms; a shift toward them lowers margin and may raise volume and returns.
- **Geographic mix** — export versus domestic, with different pricing and cost structures.
- **Channel mix** — modern trade and e-commerce carry different economics, per the distribution chapter.

**The test: has RoCE moved in the same direction as margin?** Where margin falls and RoCE rises, the mix shift is toward a less capital-intensive business and is value-accretive. Reporting the margin decline without this check produces the wrong conclusion.

### Using it in the forecast

- **Forecast each driver separately** rather than assuming a margin. This is the same discipline as the operating leverage chapter, applied to the margin line specifically.
- **Assign persistence** — reverse the cyclical components, carry the structural ones.
- **Build the forward bridge** as an output of the forecast, and sense-check it: if the model implies 300bp of margin expansion, the bridge should show where it comes from. **A model whose forward bridge cannot be explained is asserting improvement without a mechanism.**
- **Present the bridge in the note** as a table or waterfall — it is among the most useful single exhibits an analyst can publish, and it demonstrates that the forecast is built rather than assumed.

## Common mistakes
- Reporting a margin change without **decomposing** it.
- Reading a **mix-driven** margin decline as deterioration without checking returns.
- Treating **operating deleverage** as a structural problem.
- Ignoring a large unexplained **residual** in the bridge.
- Crediting **efficiency gains** that are deferred maintenance or cut advertising.
- Forecasting a margin directly rather than building it from drivers.
- Publishing a forecast whose implied margin expansion has **no identified source**.

## Interview angle
"EBITDA margin fell 220bp. Is that a problem?" Say it cannot be answered without decomposing it, then give the components: price realisation, input cost, mix, and fixed-cost absorption on volume — because each has different persistence. A price-driven decline is the serious one, since it means competitive pressure and does not self-correct; an input-cost decline is cyclical and recovery depends on the company's demonstrated pass-through record; operating deleverage on a volume shortfall is arithmetic and reverses. Then give the mix check that most people miss: if the decline is mix-driven, ask whether RoCE moved the same way, because a shift toward a lower-margin but less capital-intensive business can raise returns while lowering margin — which is good news presented badly. Finish with the forecasting discipline: build the forward margin from the same drivers rather than assuming it, and sense-check the implied bridge, because a model showing margin expansion with no identifiable source is asserting improvement without a mechanism.
