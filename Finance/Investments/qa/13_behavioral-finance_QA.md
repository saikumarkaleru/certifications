# Q&A — Behavioral Finance

Practice bank for Chapter 13. Work each question before reading the answer. Recurring theme: prices deviate from value because biases are **systematic and correlated** (they don't cancel) and because **arbitrage is limited** (mispricing survives). Both pillars are needed — remember which one you are invoking.

---

## Section A — Concept Checks

**A1. State the core claim of behavioral finance in one sentence.**
Asset prices are set by real humans subject to systematic, predictable cognitive and emotional biases, and whose ability to arbitrage those errors away is limited — so prices can deviate from fundamental value, sometimes for a long time.

**A2. Behavioral finance has two pillars. Name them and explain why *both* are required.**
Pillar one is **limited rationality** — investors make systematic (not random) errors, so mispricing is created. Pillar two is **limits to arbitrage** — smart money cannot cheaply and risklessly correct the error, so mispricing persists. Remove pillar one and there is nothing to correct; remove pillar two and rational arbitrageurs instantly erase any mispricing and the standard model reasserts itself. Biases create the gap; limits to arbitrage let it survive.

**A3. Why don't individual investors' errors simply cancel out in aggregate?**
Because the errors are **correlated**, not independent. If 10,000 investors each made an independent random mistake, the mistakes would average to roughly zero. But human brains are wired similarly, exposed to the same news, and susceptible to the same emotional contagion — so most people lean the *same* wrong way at the same time. Correlated errors accumulate and move the whole market in one direction.

**A4. Distinguish System 1 and System 2 thinking, and say where biases live.**
System 1 is fast, automatic, intuitive, emotional, and effortless — and it is where most biases live. System 2 is slow, deliberate, logical, and effortful. System 2 is "lazy" (it burns glucose and attention), so under time pressure, information overload, or emotional arousal — the normal conditions of markets — System 1 takes the wheel and biased intuition drives decisions.

**A5. State the four defining features of Prospect Theory.**
(1) **Reference dependence** — outcomes are judged as gains/losses relative to a reference point (often purchase price or status quo), not in terms of final wealth. (2) **Loss aversion** — losses hurt ~2–2.5× more than equivalent gains please. (3) **Diminishing sensitivity / S-shaped value function** — concave (risk-averse) in gains, convex (risk-seeking) in losses. (4) **Probability weighting** — small probabilities are overweighted (lottery + insurance), moderate-to-high probabilities underweighted.

**A6. What is the disposition effect, and which Prospect Theory feature drives it?**
The tendency to **sell winners too soon and hold losers too long**. It is driven by loss aversion combined with reference dependence: selling a loser forces you to "realize" the painful loss and admit a mistake, while selling a winner locks in the pleasant gain. It is backwards from optimal behavior on two counts — tax (you should harvest losses) and momentum (winners tend to keep winning).

**A7. Distinguish loss aversion from ordinary risk aversion.**
Classical **risk aversion** concerns the curvature of utility over *total wealth* and makes people prefer certainty everywhere. **Loss aversion** concerns the asymmetric pain of losses versus gains *around a reference point* — and crucially it makes people **risk-seeking in the loss domain** (they gamble to break even), which pure risk aversion can never do.

**A8. Give the anomaly-to-bias mapping for momentum versus the value premium.**
**Momentum / PEAD** is driven by *underreaction* (anchoring and conservatism make investors slow to price news), over a short horizon of 3–12 months. The **value premium / long-term reversal** is driven by *overreaction* (representativeness makes investors extrapolate too far), over a long horizon of 3–5 years. Different biases, different horizons — they do not contradict.

**A9. What is myopic loss aversion and which puzzle does it explain?**
Myopic loss aversion combines loss aversion with **frequent evaluation** of one's portfolio. An investor who checks often sees many small losses, feels the ~2.25× pain, and therefore demands a large premium to hold stocks. It explains the **equity premium puzzle** — the historically large (~5–6%) excess return of stocks over bonds that ordinary risk aversion cannot justify.

**A10. List the four main limits to arbitrage.**
(1) **Fundamental risk** — no perfect substitute to hedge with. (2) **Noise-trader risk** — the mispricing can widen before it corrects. (3) **Implementation costs** — short-selling is costly, sometimes impossible, subject to recall. (4) **Capital / horizon constraints** — arbitrageurs run other people's money and face redemptions exactly when the opportunity is best.

**A11. Distinguish cognitive biases from emotional biases and say which are easier to fix.**
**Cognitive biases** are faulty reasoning (anchoring, confirmation, availability) — often correctable with information, education, and process. **Emotional biases** are feelings that override reason (loss aversion, regret aversion) — harder to fix because awareness does not dissolve the felt panic. This is why you can *know* about loss aversion and still act on it.

**A12. Why can herding be individually rational yet collectively destabilizing?**
Herding has an *informational* basis ("everyone is buying — maybe they know something") and a *reputational* basis ("it is better to fail conventionally" — a manager wrong with the crowd keeps her job; wrong alone she is fired). Each of these can make following the crowd privately sensible, even while the aggregate result — self-reinforcing bubbles and crashes — is collectively destructive.

---

## Section B — Applied / Numerical Problems (full working)

**B1. Loss aversion rejects a positive-EV bet.**
Coin flip: heads win ₹1,000, tails lose ₹800. Evaluate with the value function using $\lambda = 2.25$ (ignore curvature).

- Expected value: $0.5(1000) + 0.5(-800) = +₹100$ — a rational agent takes it.
- Prospect-theory value: $V = 0.5\,v(1000) + 0.5\,v(-800) = 0.5(1000) + 0.5(-2.25 \times 800)$.
- $V = 500 + 0.5(-1800) = 500 - 900 = \mathbf{-400}$.

**Reconcile:** the *subjective* value is negative, so a loss-averse person **rejects** a +EV bet. This is the mechanism behind cash-hoarding and the fat equity premium. ✓

**B2. How large must the gain be to tempt the loss-averse player?**
Same flip, same $\lambda = 2.25$, but solve for the winning payoff $W$ that makes the player indifferent ($V = 0$), holding the ₹800 loss fixed.

- Set $0.5\,W + 0.5(-2.25 \times 800) = 0$.
- $0.5\,W = 0.5(1800) \Rightarrow W = 1800$.

**Reconcile:** the potential win must be **₹1,800** — more than *twice* the ₹800 potential loss — before the average person will flip. Loss aversion demands roughly a 2.25:1 gain-to-loss ratio just to break even psychologically. ✓

**B3. The disposition effect and after-tax return.**
Priya bought Stock A and Stock B at ₹100 each. Now A = ₹130 (winner), B = ₹70 (loser). She needs cash and can sell only one. Capital-gains regime: gains are taxable, realized losses are deductible against other gains. Momentum: winners tend to keep outperforming, losers to keep underperforming over 3–12 months.

- **Disposition prediction:** she sells the **winner A** (feels good, locks the gain) and holds the **loser B** ("it'll come back to ₹100").
- **Tax:** selling A triggers a taxable ₹30 gain; selling B would harvest a deductible ₹30 loss. She chose the tax-*inefficient* option.
- **Momentum:** she sold the stock more likely to rise and kept the one more likely to fall.

**Reconcile:** the correct move — sell loser B, harvest the loss, let winner A run — is the exact opposite of what loss aversion whispers. Studies estimate the disposition effect costs individual investors on the order of **1.5–4% per year**. ✓

**B4. Overconfidence and the cost of overtrading.**
Rahul turns over his ₹10,00,000 portfolio 200%/year, paying 0.5% all-in per round-trip. His stock-picking skill is genuinely zero: gross return = market's 12%. Compare to an index investor at 10% turnover paying 0.05%.

- Rahul gross: 12% → ₹1,20,000. Trading drag: $200\% \times 0.5\% = 1.0\%$ = ₹10,000. **Net 11.0%.**
- Index net: $12\% - 0.05\% \approx 11.95\%$.
- 20-year compounding: ₹10 lakh at 11.95% → ~₹94.6 lakh; at 11.0% → ~₹80.6 lakh.

**Reconcile:** a ~0.95% annual gap, driven purely by overconfidence-fueled activity with *no* skill assumed, compounds to a **~₹14 lakh penalty**. This is Barber & Odean in miniature: "trading is hazardous to your wealth." ✓

**B5. Framing flips a decision with identical math.**
An advisor pitches one structured note two ways. Frame X: "90% chance of returning your capital plus 8%." Frame Y: "10% chance of losing money." Are these the same offer, and why do clients respond differently?

- The two frames are **mathematically identical** — a 90%/10% split over the same outcomes.
- Clients accept **Frame X far more often**: the gain frame plus overweighting of the salient positive outcome makes X feel safe and Y feel dangerous.

**Reconcile:** identical facts, opposite choices — pure framing. This is why disclosure regulation increasingly mandates *both* frames and standardized risk labels to neutralize the manipulation. Personal takeaway: re-frame every decision at least two ways before acting; if your choice flips, System 1 is driving. ✓

**B6. Myopic loss aversion and evaluation frequency.**
Stocks return +1% per month on average with enough volatility that any given month is down ~40% of the time. Investor Ravi checks his portfolio *monthly*; investor Meera checks *once a year*. Using loss aversion ($\lambda = 2.25$), explain who is more likely to abandon equities.

- Ravi sees ~4–5 losing months per year, each triggering the ~2.25× pain. Frequent exposure to losses makes the felt experience of holding stocks net-painful.
- Meera evaluates on an annual horizon, where positive years dominate and losses are rarer and smaller in frequency, so the felt experience is net-positive.

**Reconcile:** the *same* asset produces very different subjective experiences purely because of **evaluation frequency**. The more often you look, the more loss aversion bites — so Ravi is far more likely to sell equities and demand a higher premium. The practical fix: look less often. ✓

---

## Section C — Interview-Style Questions (model answers)

**C1. "If markets are efficient, why does your fund exist?"**
Because efficiency is *bounded*, not absolute. Behavioral finance says two things the standard model ignores: investors have systematic, correlated psychological biases that push prices away from value, and arbitrage is too risky and capital-constrained to fully correct them. That leaves persistent, exploitable pockets — momentum from underreaction, the value premium from overreaction, sentiment-driven mispricing where short-selling is hard. My fund exists to harvest those, disciplined by the knowledge that arbitrage is risky, so I size positions to survive noise-trader risk.

**C2. "Does behavioral finance disprove the Efficient Market Hypothesis?"**
No — it refines it. Markets are approximately efficient because arbitrage genuinely works most of the time. But efficiency is bounded: when sentiment is extreme and arbitrage is constrained, prices detach from value. Behavioral finance is the loyal opposition, not a wrecking ball. The debate is settled enough that Fama, who built EMH, and Shiller, who documented excess volatility and bubbles, *shared* the 2013 Nobel Prize. The honest position is a spectrum, not a binary.

**C3. "Explain Prospect Theory as if I've never heard of it."**
Classical theory says people value final wealth and maximize expected utility. Prospect Theory, from Kahneman and Tversky, says that's not how humans actually choose. Four facts: we judge outcomes as gains or losses against a **reference point**, not absolute wealth; **losses hurt about 2.25× more** than equal gains please; the value function is **S-shaped** — risk-averse in gains but risk-*seeking* in losses, so we gamble to avoid a sure loss; and we **distort probabilities**, overweighting rare events, which is why the same person buys lottery tickets *and* insurance. Those four features explain the disposition effect, the equity premium puzzle, and most investor misbehavior.

**C4. "Give me one bias, its mechanism, and what it costs investors."**
Overconfidence. The mechanism: investors overestimate their knowledge, precision, and control — roughly 80% think they're above-average — which leads to overtrading and under-diversification. Barber and Odean studied 66,000 brokerage accounts and found the most active traders underperformed the market by about **6.5 percentage points a year** after costs; men traded ~45% more than women and earned correspondingly less. Overconfidence rises *after* a run of gains, because people credit skill rather than luck — exactly when caution is most warranted. The cure is a rules-based, low-turnover process.

**C5. "Momentum and the value premium seem to contradict each other. Do they?"**
No — they operate on different horizons and different biases. Short-term **momentum** (3–12 months) is driven by *underreaction*: anchoring and conservatism make investors slow to fully price news, so prices drift in the direction of the surprise — that's Jegadeesh and Titman, and post-earnings-announcement drift. Long-term **reversal / the value premium** (3–5 years) is driven by *overreaction*: representativeness makes investors extrapolate glamour stocks too far and punish value stocks too hard, then it reverses — that's De Bondt and Thaler. Both can be true at once because they describe different frequencies of the same news-processing error.

**C6. "Why don't hedge funds just arbitrage away the mispricings you describe?"**
Because arbitrage isn't the free lunch textbooks imply. Four frictions: **fundamental risk** — often no perfect substitute to hedge with; **noise-trader risk** — the mispricing can widen before it corrects, so you can be right and still be wiped out by margin calls; **implementation costs** — shorting is expensive, sometimes impossible; and **capital constraints** — you run clients' money, and they redeem exactly when the opportunity is best. Julian Robertson's Tiger fund shorted dot-coms too early and was forced to close in early 2000, right before the crash he correctly foresaw. Being right too soon is indistinguishable from being wrong.

**C7. "How would you protect yourself and a client from these biases?"**
Two fronts. Defense against my *own* biases: a rules-based process with pre-commitment, checklists, systematic rebalancing, low turnover, seeking the bear case to fight confirmation bias, and ignoring the purchase-price anchor. For clients: choice architecture — "nudges" like auto-enrolment use status-quo bias *for* them, and evaluating portfolios less often blunts myopic loss aversion. Offense, cautiously: disciplined value and momentum tilts and contrarian positioning against sentiment extremes, sized to survive noise-trader risk. Thaler won the 2017 Nobel for exactly this bridge from bias to policy.

**C8. "What's the single most important number in behavioral finance and why?"**
The loss-aversion coefficient, $\lambda \approx 2.25$. It says losses hurt roughly 2.25 times more than equal gains please, and that one parameter bends the whole value function. It drives the disposition effect (why we won't realize losses), the equity premium puzzle (why we over-demand compensation for holding stocks), and the general reluctance to take sensible positive-EV risk. If I can only teach a client one fact, it's that their fear of loss is quantifiably more than double their pleasure from gain — and that asymmetry, not the market, is usually their biggest enemy.

---

## Section D — MCQs (with reasoning)

**D1.** The two pillars of behavioral finance are:
(a) rational agents and efficient markets (b) systematic biases and limits to arbitrage (c) System 1 and System 2 (d) momentum and value
**Answer: (b).** Biases create mispricing; limits to arbitrage let it persist. Both are needed — remove either and the standard model reasserts itself.

**D2.** Individual investor errors move prices in aggregate because they are:
(a) random and independent (b) small (c) systematic and correlated (d) always cognitive
**Answer: (c).** Independent random errors cancel to zero. Correlated errors — shared wiring, shared news, shared emotion — accumulate and push the whole market one way.

**D3.** In Prospect Theory, the value function is:
(a) concave everywhere (b) convex everywhere (c) concave in gains and convex in losses (d) linear
**Answer: (c).** S-shaped: risk-averse (concave) in the gain domain, risk-seeking (convex) in the loss domain — the source of gambling to break even.

**D4.** The disposition effect is the tendency to:
(a) sell winners too soon and hold losers too long (b) sell losers too soon and hold winners too long (c) trade too frequently (d) chase recent performance
**Answer: (a).** Loss aversion makes realizing a loss painful, so investors cling to losers and lock in gains early — backwards on both tax and momentum grounds. Option (c) is overconfidence; (d) is recency.

**D5.** The loss-aversion coefficient $\lambda \approx 2.25$ means:
(a) gains feel 2.25× better than losses (b) losses hurt ~2.25× more than equal gains please (c) probabilities are weighted by 2.25 (d) stocks beat bonds by 2.25%
**Answer: (b).** Losses loom about 2.25 times larger than equivalent gains — the central asymmetry of behavioral finance.

**D6.** Momentum and post-earnings-announcement drift are best explained by:
(a) overreaction (b) underreaction (c) herding only (d) probability weighting
**Answer: (b).** Anchoring and conservatism make investors *slow* to fully price news, so prices drift in the surprise direction for weeks to months.

**D7.** The value premium / long-term reversal is best explained by:
(a) underreaction (b) overreaction via representativeness (c) framing (d) mental accounting
**Answer: (b).** Representativeness makes investors extrapolate glamour stocks too far and over-punish value stocks; over 3–5 years this overreaction reverses.

**D8.** Myopic loss aversion explains which puzzle?
(a) the closed-end fund discount (b) momentum (c) the equity premium puzzle (d) the January effect
**Answer: (c).** Loss aversion plus frequent evaluation makes investors demand a large premium to hold stocks — explaining the puzzlingly large historical equity premium.

**D9.** Which is NOT one of the limits to arbitrage?
(a) fundamental risk (b) noise-trader risk (c) perfect substitutes and free shorting (d) capital/horizon constraints
**Answer: (c).** That option is the *absence* of limits. The real limits are fundamental risk, noise-trader risk, implementation/short-sale costs, and capital constraints.

**D10.** A person who buys both lottery tickets and insurance is displaying:
(a) loss aversion (b) probability weighting (overweighting small probabilities) (c) anchoring (d) herding
**Answer: (b).** Overweighting rare events makes both the tiny jackpot chance and the tiny disaster chance feel larger than they are — driving lottery buying and insurance buying simultaneously.

**D11.** Loss aversion differs from classical risk aversion because loss aversion:
(a) applies only to wealthy investors (b) makes people risk-seeking in the loss domain (c) is always cognitive (d) disappears once you know about it
**Answer: (b).** Risk aversion never produces risk-seeking; loss aversion does, in the loss domain, where people gamble to avoid realizing a sure loss.

**D12.** An advisor pitches "90% chance of gaining" versus "10% chance of losing" for the same product and gets different acceptance. This is:
(a) anchoring (b) the framing effect (c) confirmation bias (d) hindsight bias
**Answer: (b).** Identical mathematics, opposite choices, driven purely by gain-versus-loss presentation — the definition of framing.

**D13.** "The market can remain irrational longer than you can remain solvent" is the practical statement of:
(a) the equity premium puzzle (b) noise-trader risk / limits to arbitrage (c) mental accounting (d) System 1 dominance
**Answer: (b).** It captures noise-trader risk: an arbitrageur can be correct yet be forced to liquidate before the mispricing corrects.

---

*End of Chapter 13 Q&A. Master three reflexes: (1) always name **which pillar** you're invoking — biases create mispricing, limits to arbitrage let it survive; (2) keep $\lambda \approx 2.25$ and the anomaly→bias→horizon table on instant recall; (3) frame behavioral finance as *refining*, not disproving, EMH — bounded efficiency, Fama and Shiller sharing one Nobel.*
