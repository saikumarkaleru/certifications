# Q&A — Corporate and Business Strategy for Analysts

A practice bank for Chapter 37. Work each question before reading the answer. The theme throughout is the chapter's core claim: **strategy analysis and valuation are the same analysis viewed from two ends** — a company earns value only from a positive ROIC-minus-WACC spread, competition erodes that spread, and a moat is what slows the erosion. Every Section B number is reproducible by hand with the identity **g = ROIC × Reinvestment Rate**, so you can prove each answer without a spreadsheet.

---

## Section A — Concept-Check

**A1. In one sentence, why is a well-linked, internally consistent model still capable of being "worthless"?**

Because a model is a theory of the business expressed in arithmetic, and the arithmetic can be flawless while the theory is empty. If the growth rate, margin and reinvestment assumptions have no competitive justification — no answer to "why this number and not another?" — the model is a guess dressed in decimal places, and it will be confidently, precisely wrong.

**A2. What single condition must hold for a company to create value, and why does growth alone not create value?**

The company must earn a return on invested capital (ROIC) above its weighted average cost of capital (WACC). Value comes from the *spread*, ROIC − WACC. If a company earns exactly its cost of capital, every rupee it reinvests returns precisely what investors demanded, so growth adds nothing — it is running to stand still. Worse, if ROIC < WACC, growth actively destroys value because each reinvested rupee returns less than it cost.

**A3. State the "law of convergence" and its consequence for forecasting.**

Excess profits attract competition, and competition erodes excess profits — capital is mobile and greedy, so a business earning 40% ROIC in an unprotected market invites entrants until returns fall back toward the cost of capital. The consequence: the *default* forecast for any high-ROIC business is that its returns fade toward WACC over 5–15 years. Sustained excess returns are the exception that must be explained, not the assumption.

**A4. What is a moat, and how does it relate to the law of convergence?**

A moat is a structural barrier that raises the cost or lowers the payoff of competing, so rivals rationally decline (or try and fail). It does not repeal convergence — it slows it. That is exactly why moat analysis maps onto the *fade period* in a model: a wide-moat business fades slowly (long competitive advantage period), a no-moat business fades fast.

**A5. Name the five sources of moats and give the model signature of each.**

- **Intangible assets** (brands, patents, licences) → high, stable gross margin; pricing power above inflation.
- **Switching costs** → high retention, low churn, recurring revenue, pricing power.
- **Network effects** → increasing returns to scale, winner-take-most share, expanding margins with scale.
- **Cost advantage** (scale, process, location, unique asset) → higher margin than peers at the same price; ability to survive price wars.
- **Efficient scale** (market supports only one or few players) → stable oligopoly margins, rational pricing, low new entry.

**A6. Porter's Five Forces reduces to what single analytic question?**

"How much of this industry's profit is protected, and for how long?" Each force is a channel through which returns leak: powerful buyers bargain margins down, powerful suppliers bargain costs up, new entrants and substitutes take volume, and rivalry does all of the above. Benign forces → excess returns persist → high, stable modeled margins. Hostile forces → thin, volatile, mean-reverting margins.

**A7. Map the three components of value creation to the three model parameters they drive.**

- **How high** the spread is → drives forecast **margins and ROIC**.
- **How long** it lasts → drives the **length of the high-growth window and the fade** to terminal value.
- **How fast the business grows while earning the spread** → drives the **reinvestment rate** and therefore free cash flow.

**A8. How does the value chain sharpen a claimed competitive advantage?**

A competitive advantage must live in a *specific activity*, and that activity must show up in a *specific line* of the model. If a firm claims a cost advantage, you ask *which* activity is cheaper — procurement (→ lower COGS), operations (→ higher gross margin), or distribution (→ lower SG&A) — then check whether historical, peer-relative margins corroborate it. A firm that claims a process cost advantage but shows peer-average gross margins does not have one; do not model one.

**A9. State the rule that makes SWOT rigorous rather than decorative.**

Every SWOT entry must carry a model consequence or it does not belong on the page. And the sharper rule: **Strengths and Weaknesses set the *level* of returns (where margins start); Opportunities and Threats set the *durability* of returns (how they evolve).** The first pair are internal and present; the second pair are external and future, and are usually modeled as scenario upside/downside rather than the base case.

**A10. Why is customer concentration a modeled risk, and to which of the Five Forces does it belong?**

It belongs to the **bargaining power of buyers**. A single customer representing more than ~10% of revenue can bargain pricing down and can walk, capping gross margin and adding volatility. It is modeled explicitly — as a pricing constraint, a scenario in which the customer is lost, and often a higher discount rate for the added business risk.

**A11. What is the single most common overvaluation error, and its one-line fix?**

Holding ROIC far above WACC into the terminal year — an "immortal moat" that assumes the company defeats competition forever. Fix: fade terminal ROIC toward WACC unless you can defend permanence out loud; almost nothing is permanent.

---

## Section B — Applied / Build Problems

**B1. Compute ROIC and the value spread.**

A company reports EBIT of ₹150 Cr, a tax rate of 25%, and invested capital of ₹500 Cr. Its WACC is 10%. Find NOPAT, ROIC, and the spread. Is value being created?

*Answer, step by step:*
1. NOPAT = EBIT × (1 − tax rate) = 150 × (1 − 0.25) = 150 × 0.75 = **₹112.5 Cr**.
2. ROIC = NOPAT / Invested Capital = 112.5 / 500 = **22.5%**.
3. Spread = ROIC − WACC = 22.5% − 10% = **12.5%**.
4. The spread is positive and large, so **value is being created** — consistent with a genuine competitive advantage. The next question is durability (how long the 12.5% lasts).

**B2. Chain growth to reinvestment.**

Using the company in B1 (ROIC 22.5%), you forecast base-case revenue and NOPAT growth of 10%. What reinvestment rate does that require, and what is year-1 FCFF?

*Answer:*
1. Rearrange g = ROIC × Reinvestment Rate → Reinvestment Rate = g / ROIC = 0.10 / 0.225 = **0.4444 (≈ 44.4%)**.
2. FCFF = NOPAT × (1 − Reinvestment Rate) = 112.5 × (1 − 0.4444) = 112.5 × 0.5556 = **₹62.5 Cr**.
3. Interpretation: because ROIC is high, the firm grows 10% *and* still converts ~56% of NOPAT to cash. That cash-generative growth is the moat showing up in the numbers.

**B3. The reinvestment-reconciliation trap.**

A junior analyst forecasts 15% NOPAT growth while assuming a reinvestment rate of only 5%. What ROIC is that combination silently claiming, and why should it alarm you?

*Answer:*
1. From g = ROIC × Reinvestment Rate → ROIC = g / Reinvestment Rate = 0.15 / 0.05 = **3.0 = 300%**.
2. A 300% ROIC is implausible for virtually any real business — it would broadcast the loudest possible signal to competitors. The model is silently claiming a moat wider than any that exists.
3. The lesson: growth and reinvestment are **chained, not independent**. Setting them separately is how analysts smuggle in an impossible ROIC. Always back out the implied ROIC and sanity-check it.

**B4. When growth destroys value.**

A capital-hungry firm earns ROIC of 8% against a WACC of 10% and plans to grow NOPAT at 6%. Compute the required reinvestment rate and explain what growth does to value here.

*Answer:*
1. Reinvestment Rate = g / ROIC = 0.06 / 0.08 = **0.75 (75%)**.
2. FCFF = NOPAT × (1 − 0.75) = NOPAT × 0.25 — three-quarters of profit is consumed just to fund the growth.
3. Because ROIC (8%) is *below* WACC (10%), every reinvested rupee returns less than it cost. **Growth destroys value**: the faster this firm grows, the more value it burns. The value-maximizing move for a below-WACC business is to reinvest *less* and return cash, not to chase growth.

**B5. Peer-relative corroboration.**

BrewCo, a premium coffee brand, shows a 15% EBIT margin. Its commodity-coffee peers average 12%. BrewCo claims a brand moat located in marketing/brand. Does the evidence support modeling above-peer margins, and where must the advantage *not* be modeled?

*Answer:*
1. BrewCo earns roughly **3 percentage points** of EBIT margin above peers (15% vs 12%). The brand premium (₹600/kg vs ₹350 commodity) plausibly explains extra margin — the story and the numbers agree, so an above-peer gross/EBIT margin is defensible.
2. The advantage lives in **marketing/brand** (sustains the price premium) and **subscription operations** (recurring revenue → retention). It does **not** live in **procurement** — BrewCo buys green beans at market like everyone else. So you model above-peer pricing/margin but **ordinary input costs**, with explicit sensitivity to bean-price spikes (supplier-side commodity risk).

**B6. Set the fade and run the terminal sanity check.**

BrewCo currently earns ROIC of 22.5% against WACC of 10%, from a moderate, stable (not widening) brand moat. Propose a competitive-advantage period and terminal ROIC, then run the sanity check. Why does this single judgement swing the valuation so much?

*Answer:*
1. A moderate, stable moat does not last forever — substitutes and rivals press in. A defensible structure: **~8 years** of ROIC above WACC, then fade ROIC from 22.5% toward **~12%** over years 9–15, with growth slowing to a terminal **~4%** (roughly nominal GDP).
2. Sanity check: terminal ROIC 12% vs WACC 10% = a **2-point permanent spread**. Defensible *only* if the brand is genuinely enduring. If uneasy, fade terminal ROIC all the way to 10% (WACC) — assume competition eventually wins completely.
3. The gap between "12% forever" and "fades to 10%" is often **20–30% of the total valuation**, because the terminal value dominates a DCF and the terminal spread drives it. That is precisely why the *strategic judgement*, not the spreadsheet mechanics, drives the answer.

**B7. Turn a threat into numbers (scenario construction).**

For BrewCo, translate this threat into a bear case: a green-bean price shock coincides with a well-funded entrant that erodes the brand premium. Which Five Forces are firing, and what specific driver changes encode the bear case?

*Answer:*
1. Two forces fire together: **supplier power** (volatile green-coffee commodity → input-cost spike) and **threat of new entrants** (well-funded rival attacks the premium).
2. Encode as driver changes, not vibes: EBIT margin falls from 15% to **~11%** (premium compressed + costs up), and the competitive-advantage period shortens from 8 years to **~5 years** (the entrant accelerates convergence). Growth may also slow as share is contested.
3. This is the discipline: a SWOT threat becomes a *numeric* scenario. The bull mirror-image (subscription penetration rising to ~60%, deepening switching costs) would push margin toward ~17% and extend the fade to ~11 years.

---

## Section C — Interview-Style Questions

**C1. "Walk me through how you'd set the growth rate in a DCF — and don't just say 'GDP plus a bit.'"**

Model answer: I never pick growth in isolation; I derive it from a competitive story and reconcile it with reinvestment. First I size the market and the company's realistic share trajectory — growth has to come *from* someone, so I ask who loses the share we gain and why they can't stop us. That "why" is the moat. Then I check the identity g = ROIC × Reinvestment Rate — 10% growth at a 22% ROIC commits me to reinvesting about 44% of NOPAT, so the capex and working-capital lines must reflect that. Finally I fade growth toward nominal GDP over the competitive-advantage period, because the law of convergence says excess growth doesn't last. So it isn't "GDP plus a bit" — it's a share story, chained to reinvestment, fading on a schedule set by moat durability.

**C2. "This company earns a 25% ROIC. Great business — should we pay up for it?"**

Model answer: A great *company* is not automatically a great *investment* — that depends on price. Two things matter beyond the headline ROIC. First, durability: is the 25% protected by a real moat (intangibles, switching costs, network effects, cost advantage, efficient scale), and is that moat widening, stable, or narrowing? A 25% ROIC with no moat is a countdown to convergence. Second, what's already in the price: the current multiple embeds the market's assumed moat. If the market is already pricing a 15-year fortress and I think it's an 8-year moderate moat, it's overvalued despite being wonderful. My edge is the *gap* between my strategic assessment and the moat implied by the current price — not admiring the ROIC.

**C3. "How does Porter's Five Forces actually change a number in your model? Be specific."**

Model answer: I end each force with a one-line numeric implication, not an essay. Low threat of new entrants (high barriers) → hold or raise margins and lengthen the fade. Concentrated buyers → cap pricing and flag any customer above ~10% of revenue as a scenario risk. Powerful suppliers or scarce inputs → add input-cost sensitivity and stress margin under inflation. Cheap or improving substitutes → cap both the price and growth ceilings, and watch the terminal value, because a better substitute can collapse it. Fragmented, undifferentiated rivalry → thin, volatile margins that mean-revert fast. The output isn't a slide; it's a verdict on where sustainable margins sit and how quickly they fade.

**C4. "Where does business risk show up — only in the cash flows, or somewhere else too?"**

Model answer: Both, and people forget the second. A fragile competitive position — cyclical demand, a contestable market, concentrated customers — obviously lowers and destabilizes the forecast cash flows. But it also raises the *discount rate*: higher business risk feeds beta and therefore WACC. So a weak moat should hit the valuation twice: lower, more volatile cash flows *and* a higher cost of capital. Modeling only the cash-flow side understates the penalty. Conversely, a very stable, wide-moat utility-like business earns a lower discount rate as well as steadier flows.

**C5. "Defend your terminal value. Why should I believe it?"**

Model answer: The terminal value is where overvaluation hides, so I discipline it with the law of convergence. In the terminal year I push ROIC toward WACC unless I can defend a permanent spread out loud — a high bar, because almost nothing is permanent. If I keep a 2-point terminal spread, I state exactly why competition never fully wins: a durable brand, a regulatory licence, entrenched network effects. If I can't say it convincingly, I fade ROIC to WACC. I also check terminal growth isn't above nominal GDP, since no company outgrows the economy forever. The terminal value is a *claim about competition*, made explicit rather than letting a Gordon-growth formula smuggle in immortality.

---

## Section D — Common-Error Spotting

For each, identify the error and give the fix.

**D1.** "Revenue grows 8% a year to the terminal year because that's roughly what the last three years did."

Error: the **orphan growth rate** — a number with no market-size, share, or moat justification, and no fade. Fix: derive growth from a share story ("from whom, and why can't a rival take it?"), and fade it toward nominal GDP over the competitive-advantage period. The past is a reality check, not a forecast.

**D2.** A model holds ROIC at 30% flat, forever, into perpetuity, with WACC at 9%.

Error: the **immortal moat** — a permanent 21-point spread assumes the company defeats competition forever. This is the top cause of overvaluation, and the error compounds through the dominant terminal value. Fix: fade ROIC toward WACC across the competitive-advantage period; keep a terminal spread only with an explicit, defensible reason for permanence.

**D3.** Forecast: 15% NOPAT growth, 5% reinvestment rate, "because the business is capital-light."

Error: **decoupling growth and reinvestment.** g / Reinvestment = 0.15 / 0.05 = 300% implied ROIC — impossible. Fix: chain them with g = ROIC × Reinvestment Rate and confirm the implied ROIC is believable before trusting the growth number.

**D4.** The SWOT slide lists "strong management team" and "emerging regulatory risk," but neither appears anywhere in the driver assumptions.

Error: **SWOT as decoration** — entries with no model consequence. Fix: delete any SWOT item that doesn't touch a cell, or convert it into one — e.g., "emerging regulatory risk" → a bear scenario with a shortened fade and compressed margin.

**D5.** A Five Forces analysis is neatly filled in on page 4; the model on page 12 uses flat 20% margins that ignore the "high supplier power, cheap substitutes" verdict.

Error: **framework theater** — running the framework as a compliance exercise, then modeling on vibes. Fix: end each force with a one-line numeric implication and make the model reflect it (here: input-cost sensitivity plus a capped price/growth ceiling and faster fade).

**D6.** "This is a fantastic business with a wide moat, so it's a buy at any reasonable price."

Error: **confusing a good company with a good investment.** A wide moat already priced in is not an opportunity. Fix: compare your strategic assessment against the moat *implied* by the current price/multiple; the edge is in the gap, not the quality.

**D7.** The write-up claims a "clear process cost advantage," but the company's gross margin sits exactly at the peer average.

Error: **advantage with no home in the P&L.** A real cost advantage would appear as an above-peer margin line. Fix: if peer-relative margins don't corroborate the advantage, don't model one — locate every claimed edge in a specific value-chain activity and verify it against history.

**D8.** The base case treats an uncertain outcome — "the new entrant will fail" — as a certainty, with no downside version.

Error: a **single-point strategic bet** on a contested competitive outcome. Fix: express the uncertainty as bear/base/bull scenarios (entrant succeeds / stalemate / entrant fails) so the risk is visible in the valuation rather than buried in one confident number.

**D9.** "Every peer's ROIC has faded over a decade, but ours will stay elevated — no need to justify it."

Error: **ignoring the base rate of convergence.** Assuming this firm is the exception without evidence. Fix: the burden of proof is on permanence, not on decline — either produce the specific structural reason the moat resists convergence, or fade returns like the peers.

---

## Self-Check Summary

- **Core identity used throughout:** g = ROIC × Reinvestment Rate ⇒ FCFF = NOPAT × (1 − g/ROIC). Verified numerically in B1–B4 (e.g., ROIC 22.5%, g 10% → reinvestment 44.4% → FCFF ₹62.5 Cr).
- **Central thesis:** value = (ROIC − WACC) spread × durability × growth (only if ROIC > WACC); strategy sets the spread's *size* (margins/ROIC) and *durability* (fade), and growth is chained to reinvestment.
- **Frameworks as forecasting tools:** Five Forces → where margins sit and how fast they revert; value chain → which P&L line the advantage lives in; SWOT → level (S/W) vs durability (O/T), every entry with a model consequence.
- **Cardinal sin guarded against in D2/C5:** terminal ROIC far above WACC with no defence of permanence.

Every Section B figure is reproducible by hand; the arithmetic has been re-derived above.
