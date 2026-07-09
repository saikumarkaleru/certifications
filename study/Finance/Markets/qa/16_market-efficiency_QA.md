# Q&A — Market Efficiency and Price Discovery

Companion practice bank for Chapter 16. Every question is followed by a full answer. Section A checks concepts, B applies them to numbers and situations, C rehearses interview questions with model answers, and D sharpens judgement through MCQs with reasoning.

---

## Section A — Concept Check

**A1. State the Efficient Market Hypothesis (EMH) in one sentence, and unpack the two words that do the heavy lifting.**

EMH says a market is efficient with respect to a set of information if **prices already fully reflect that information, so you cannot earn abnormal risk-adjusted returns by trading on it.** The two load-bearing words are "**abnormal**" and "**information set**." "Abnormal" means *risk-adjusted* — earning 15% is no proof of skill if you bore 15%-worth of risk; efficiency never claims you can't make money, only that you can't beat what your risk warrants. "Information set" means efficiency is graded, not absolute — a market can perfectly reflect past prices yet ignore an obscure footnote, which is exactly why EMH comes in three forms.

**A2. What is price discovery, and what is the mechanism that carries it out?**

Price discovery is the process by which the continuous tug-of-war between buyers and sellers converts scattered private information and beliefs into a single public number — the market price. The mechanism is the **exchange order book**: participants post limit orders (bids and asks), the best bid and ask define the current price, and when news breaks traders cancel stale orders and repost at new levels, shifting the whole book within milliseconds. Arbitrageurs and high-frequency traders make this adjustment near-instantaneous for liquid stocks. The profit opportunity destroys itself in the act of being exploited.

**A3. Define the three forms of EMH and name the type of analysis each one defeats.**

**Weak form:** prices reflect all information in past prices and volume → defeats **technical analysis** (chart patterns, moving averages, momentum indicators built purely from price history). **Semi-strong form:** prices reflect all publicly available information → defeats **fundamental analysis** of public data (earnings, filings, macro). **Strong form:** prices reflect all information, public *and* private/insider → defeats even insider trading. Each stronger form nests the weaker ones and adds a larger information set.

**A4. Why is the phrase "the news that moves price is the surprise, not the number" central to semi-strong efficiency?**

Because in a semi-strong-efficient market, *expected* information is already in the price. Only the *unexpected* component — the deviation from consensus — is genuinely new and forces repricing. A company reporting 40% profit growth can *fall* if the market expected 50%, and a struggling firm can rally on "less bad than feared" results. This is why "good company ≠ good stock": quality is already priced, so future abnormal returns depend on outcomes relative to what was already discounted, not on absolute performance.

**A5. What is the random-walk idea, and how does it relate to weak-form efficiency?**

The random-walk idea says successive price *changes* are essentially unpredictable, because tomorrow's move depends on tomorrow's news, which by definition is not yet known. Price *levels* wander like a drunk's walk; the *next step* is roughly a coin flip around the expected-return drift. This is the mathematical backbone of weak-form efficiency: if past prices contained an exploitable signal about the next move, traders would already have acted on it and erased the pattern. Weak form is essentially the random-walk hypothesis dressed in economic clothing.

**A6. Explain the Grossman-Stiglitz paradox in plain terms.**

If markets were *perfectly* efficient, prices would reflect all information, so no one could profit from research — but then no one would bother to gather information, and prices would reflect nothing. Efficiency therefore requires a state where prices are *almost* efficient, leaving just enough profit to pay the researchers who keep them efficient. This is the "impossibility of perfectly efficient markets": the market must be *slightly* inefficient to reward the very activity that makes it efficient. Real markets live in this equilibrium — highly efficient, but not perfectly so.

**A7. What is the joint-hypothesis problem, and why does it make EMH so hard to disprove?**

To label a return "abnormal," you need a model of "normal" return (CAPM, Fama-French). So every test of efficiency is *simultaneously* a test of "markets are efficient" AND "my risk model is correct." When you find an apparent anomaly, you can never be sure whether the market is truly inefficient or your risk model is simply wrong or incomplete. Fama himself stressed this — it makes EMH nearly impossible to definitively falsify, because any rejection can be blamed on the risk model rather than on efficiency.

**A8. Why does the existence of insider-trading law tell you strong-form efficiency is false?**

If markets were strong-form efficient, private information would already be in the price and therefore worthless — there would be nothing to gain from trading on inside knowledge and no reason to regulate it. The fact that lawmakers criminalise insider trading (SEBI PIT Regulations 2015, US SEC Rule 10b-5) is an implicit admission that inside information *is* exploitable. Studies of insiders' legally disclosed trades confirm they earn abnormal returns on their own-company stock. The law exists precisely to *enforce the absence* of strong-form efficiency.

---

## Section B — Applied / Scenario Questions

**B1. Infosys is expected to report EPS of ₹16; it reports ₹18 and raises guidance. A retail investor reads the headline at 6 pm and buys at the next morning's open. In a semi-strong market, what return can they expect from the surprise, and why?**

Essentially **none** from the surprise itself. The moment the results hit the exchange filing system around 3:45 pm, informed traders reprice the stock within seconds — it may gap up 6–8% to the new fair value. By the time the retail investor buys at the next open, that adjustment is already in the price; they pay the post-news price and capture no abnormal return. They still earn the stock's normal expected return going forward for bearing risk, but the "obvious" opportunity from the good news was competed away before they could act. *Anomaly twist:* post-earnings-announcement drift (PEAD) means in reality the price often keeps drifting up for weeks — a documented crack in semi-strong efficiency.

**B2. Over 15 years, roughly 85% of active large-cap funds trail their index after fees. Explain why using Sharpe's arithmetic, and why this is evidence for efficiency.**

Before costs, the *average* actively managed rupee must earn exactly the market return, because active investors collectively *are* a large slice of the market — this is William Sharpe's "Arithmetic of Active Management," a mathematical identity, not an empirical claim. After subtracting higher active fees (say 1–2% versus 0.05% for an index fund), the average active rupee must therefore *underperform* the average passive rupee. This shows up as a large majority of active funds trailing the benchmark. It is powerful *indirect* evidence for efficiency: if large-caps like Reliance, HDFC Bank and TCS are heavily researched and near-efficiently priced, there is little mispricing left for active skill to harvest, so fees dominate the outcome.

**B3. An investor points to Warren Buffett's six decades of outperformance as proof EMH is false. Give the three-part efficiency-camp rebuttal.**

(1) **Chance:** with millions of investors, a bell curve guarantees a few extreme long-run winners by luck alone — some coin-flippers always produce long streaks of heads. (2) **Factor exposure:** AQR's "Buffett's Alpha" study showed his returns largely reflect systematic tilts — cheap (value), high-quality, low-volatility stocks levered with cheap insurance float — that can be substantially *replicated by known factors*, meaning they are compensation for identifiable risks, not inexplicable magic. (3) **Self-endorsement:** Buffett himself recommends index funds for ordinary investors and instructed his estate to put 90% into an S&P 500 index fund. The balanced verdict: markets are highly efficient for almost everyone, yet a rare, disciplined operator can exploit the residual inefficiency — both statements can be true.

**B4. In the 2021 GameStop episode the stock rocketed from ~$20 to ~$480 with no fundamental change, then collapsed. What does this show about price discovery and "limits to arbitrage"?**

It shows price discovery can *temporarily fail* under coordinated herd buying and a short squeeze — price detached from any reasonable estimate of value. It is a vivid illustration of **limits to arbitrage**: rational short-sellers who "knew" the stock was overpriced could not simply correct it. As the price rose, their losses mounted and margin calls forced them to *cover* (buy back), pushing the price even higher; some were bankrupted before they could be proven right. The lesson: "the market can stay irrational longer than you can stay solvent" — being right but early can be indistinguishable from being wrong, which is why mispricings sometimes persist.

**B5. SPIVA shows a *larger* share of active managers beat their benchmark in Indian small-caps than in large-caps. Is this a contradiction of EMH? Explain.**

No — it is exactly what the efficiency framework predicts. Efficiency is a **spectrum, not a switch**, driven by liquidity, analyst coverage and information flow. Large-caps are heavily researched, liquid and near-efficiently priced, leaving little mispricing for skill to exploit, so fees dominate and most active funds lose. Small- and micro-caps are thinly covered, less liquid and more prone to mispricing, so genuine research can find bargains and a larger share of active managers add value. The pattern *confirms* the theory: active management pays off where markets are less efficient and fails where they are highly efficient.

**B6. A quant fund builds a strategy on a newly published anomaly. Historically anomaly returns shrink ~58% after publication (McLean & Pontiff). Explain why, and what it says about EMH.**

Once an anomaly is published, traders pile in to harvest it — buying the cheap leg and selling the expensive leg — which pushes prices back toward fair value and shrinks the very return that defined the anomaly. This decay *is efficiency working in real time*: the market self-corrects once the free lunch is widely known. It also warns the quant fund that backtested profits may not survive live trading. The anomalies that *do* persist tend to be protected by risk (they are genuine risk premia), by transaction costs, or by limits to arbitrage — not by being easy free money.

**B7. A trader insists a "head and shoulders" chart pattern reliably predicts the next move. What does weak-form efficiency and the evidence say, and what is the one robust exception?**

Weak-form efficiency says price history is already reflected in the current price, so chart-only strategies should not beat buy-and-hold after transaction costs — and decades of tests broadly confirm this. Patterns are easy to see *in hindsight*; reliably predicting the *next* move from price history alone is the part that fails, and the pattern would vanish if it truly worked because everyone would trade on it. The one robust exception is **momentum** — past 3–12 month winners tend to keep winning — but this is better understood as a risk/behavioural *factor* than as "reading charts," and even it can reverse sharply and carries real risk.

**B8. Value stocks (low P/B, low P/E) have historically beaten glamour stocks. Give both the "inefficiency" interpretation and the "risk premium" interpretation.**

The **inefficiency** reading (behavioural): investors over-extrapolate the past — bidding glamour stocks too high on optimism and pushing value stocks too low on pessimism — so value later outperforms as prices mean-revert; public ratios predict returns, violating semi-strong efficiency. The **risk-premium** reading (Fama-French): value stocks are cheap *because they are riskier* — often financially distressed firms with higher exposure to bad economic states that CAPM's single beta misses; their higher average return is fair compensation, not a free lunch. Fama-French fold this into the three- and five-factor models. The joint-hypothesis problem means we cannot definitively say which is correct — that is why the debate never fully resolves.

---

## Section C — Interview-Style Questions (with model answers)

**C1. "Explain the three forms of the Efficient Market Hypothesis and give the current empirical verdict on each."**

*Model answer:* Eugene Fama classified efficiency by the information set prices reflect, in three nested forms. **Weak form** — prices reflect all past price and volume data, so technical analysis can't beat the market; this is the *best-supported* form, though momentum is a stubborn documented exception. **Semi-strong form** — prices reflect all public information, so fundamental analysis of public data can't earn abnormal returns and prices adjust rapidly and fully to news; it holds broadly for liquid large-caps, with post-earnings-announcement drift and the value/size effects as the notable cracks. **Strong form** — prices reflect public *and* private information, so even insiders can't profit; this is *rejected*, and the existence of insider-trading law is the proof — insiders demonstrably earn abnormal returns on their own-company trades. The honest summary: markets are highly efficient but not perfectly so, and efficiency is a spectrum that varies by liquidity and information quality.

**C2. "If markets are efficient, why do active fund managers exist at all — and should I ever pay for one?"**

*Model answer:* Three reasons they exist. First, Grossman-Stiglitz: markets are only *almost* efficient, and someone must be paid to do the research that keeps them efficient — active managers are that someone, competing for the residual profit. Second, efficiency is a spectrum: in less efficient corners like small-caps, emerging markets and private assets, genuine skill can add value, and SPIVA data confirm more active managers beat benchmarks there. Third, many investors hire managers for reasons beyond alpha — risk management, behavioural coaching, tax and liability matching. Should *you* pay for one? For core exposure to liquid large-caps, no — Sharpe's arithmetic says the average active rupee underperforms after fees, so default to low-cost passive. Pay for active management only where the market is genuinely less efficient *and* you can identify a manager with a durable, evidence-based edge in advance — which is rare and hard.

**C3. "A stock crashes 40% in a day. Doesn't that prove markets are irrational and inefficient?"**

*Model answer:* Not by itself. Efficiency does not mean prices are always *correct* — it means they are *unbiased* and reflect available information, right on average with errors you can't systematically predict in advance. A 40% drop is fully consistent with efficiency if genuinely new, adverse information arrived — a fraud revelation, a guidance cut, a regulatory shock — and the market repriced quickly to the new fair value. That is price discovery working, not failing. What *would* challenge efficiency is if the drop were *predictable* beforehand, or if it drifted further in a forecastable way afterward, or reversed in a systematic pattern. Big moves reflect the arrival of big information, and hindsight makes any price look "wrong." The real test is predictability, not volatility.

**C4. "How do regulators like SEBI and the SEC try to engineer market efficiency?"**

*Model answer:* They target the two efficiency forms deliberately. To *promote* semi-strong efficiency, they mandate fast, fair, simultaneous public disclosure — SEBI's LODR listing rules and the SEC's Regulation FD ensure material information reaches all investors at once rather than leaking to a favoured few, so public prices track reality. To *enforce the absence* of strong-form efficiency, they criminalise trading on undisclosed private information — SEBI's PIT Regulations 2015 and SEC Rule 10b-5 — levelling the field so insiders can't systematically exploit the public. They also underpin *price discovery* itself through market-microstructure rules: transparent order books, circuit breakers, surveillance against manipulation, and liquidity requirements. The common thread is that efficiency is not automatic — it is an engineered outcome of disclosure, fair access and enforcement, which is why weak enforcement regimes show weaker efficiency.

**C5. "You believe in EMH but you also run a stock-picking side portfolio. Reconcile that."**

*Model answer:* There is no contradiction if I am honest about *where* and *why*. I hold my core wealth in low-cost index funds because for liquid large-caps the evidence is overwhelming — Sharpe's arithmetic and SPIVA say the average active rupee loses after fees, and I have no reason to think I'm systematically above average there. My stock-picking is confined to areas where efficiency is genuinely looser — under-covered small-caps or special situations — where mispricing is more plausible, and I size it small and treat it partly as tuition and engagement. Crucially, I judge it on *risk-adjusted* returns against the right benchmark, not raw gains, because beating the market by taking more risk isn't skill. And I stay alert to the joint-hypothesis problem and to luck: a few good years prove nothing. The framework tells me to be humble by default and to demand real evidence of an edge before betting on one.

---

## Section D — Multiple-Choice Questions (with reasoning)

**D1. Which form of EMH, if true, would make technical analysis useless?**
(a) Only the strong form
(b) The weak form (and therefore all stronger forms)
(c) Only the semi-strong form
(d) No form addresses technical analysis

**Answer: (b).** Technical analysis uses only past prices and volume, exactly the information set of the weak form. If even the weak form holds, that information is already in the price and technical analysis can't beat the market — and since stronger forms nest the weak form, they defeat it too.

**D2. In a semi-strong-efficient market, what drives the price reaction to an earnings report?**
(a) The absolute level of reported profit
(b) The surprise — the deviation from consensus expectations
(c) The company's dividend history
(d) The volume traded on the day

**Answer: (b).** Expected information is already priced; only the unexpected component is new. A firm can beat last year handsomely yet fall if it missed expectations, and vice versa — "good company ≠ good stock."

**D3. The Grossman-Stiglitz paradox implies that:**
(a) Markets are always perfectly efficient
(b) Markets can never be efficient at all
(c) Markets must be slightly inefficient to reward the research that keeps them efficient
(d) Insider trading should be legal

**Answer: (c).** If prices reflected everything, no one would be paid to gather information, so prices would reflect nothing. Equilibrium requires just enough inefficiency to compensate researchers — "the impossibility of perfectly efficient markets."

**D4. Strong-form efficiency is generally considered:**
(a) The best-supported form empirically
(b) True for large-cap stocks only
(c) False, which is why insider-trading laws exist
(d) Untestable in principle

**Answer: (c).** Insiders demonstrably earn abnormal returns on their own-company trades; if strong form held, private information would be worthless. The existence and enforcement of insider-trading law is the practical admission that strong form is false.

**D5. The joint-hypothesis problem states that any test of market efficiency is simultaneously a test of:**
(a) The company's accounting quality
(b) The asset-pricing (risk) model used to define "normal" return
(c) The exchange's trading hours
(d) The investor's tax bracket

**Answer: (b).** "Abnormal" return is defined relative to a model of normal return (CAPM, Fama-French). So a rejection of efficiency could equally be a rejection of the risk model — you can never disentangle the two, which makes EMH extremely hard to falsify.

**D6. That ~85% of active large-cap funds trail their index after fees is best explained by:**
(a) Active managers being unusually incompetent
(b) Sharpe's arithmetic — the average active rupee earns the market return minus higher fees
(c) Index funds taking on hidden leverage
(d) Survivorship bias alone

**Answer: (b).** By identity, the average active dollar earns the market return before costs, so after higher fees it must underperform the average passive dollar. It is a mathematical certainty, not a comment on manager IQ.

**D7. Post-earnings-announcement drift (PEAD) is an anomaly that most directly challenges:**
(a) Weak-form efficiency
(b) Semi-strong-form efficiency
(c) Strong-form efficiency
(d) The random-walk hypothesis for volume

**Answer: (b).** Semi-strong efficiency predicts prices adjust to public earnings news *instantly and completely*. PEAD — prices continuing to drift in the surprise's direction for weeks — shows adjustment is neither instant nor complete, a documented crack in the semi-strong form.

**D8. McLean & Pontiff found published anomaly returns shrink ~58% after publication. This is best interpreted as:**
(a) Proof that all anomalies were fake
(b) Evidence that markets are hopelessly inefficient
(c) Efficiency at work — traders arbitrage the anomaly away once it is known
(d) A data error

**Answer: (c).** Publicising a free lunch invites traders to exploit it, pushing prices back to fair value and shrinking the return. The decay is efficiency self-correcting in real time — though the residual (~42%) suggests some anomalies are genuine risk premia or protected by limits to arbitrage.

**D9. "Efficient markets" most precisely means that prices are:**
(a) Always exactly equal to true intrinsic value
(b) Unbiased and reflect available information, with errors you can't predict in advance
(c) Never volatile
(d) Set by regulators

**Answer: (b).** Efficiency means prices are *right on average* and unpredictable in their errors, not literally correct at every moment. Prices are constantly "wrong" in hindsight; efficiency only says you can't forecast the direction of the error beforehand.

**D10. The value and size effects are defended by the efficiency camp as:**
(a) Proof that fundamental analysis always works
(b) Risk premia — compensation for risks CAPM misses, folded into multi-factor models
(c) Violations of the weak form
(d) Evidence for strong-form efficiency

**Answer: (b).** Fama-French argue value and small-cap stocks earn more because they are riskier (e.g., distress risk) in ways a single CAPM beta doesn't capture. Recast as risk premia, they are fair compensation rather than free lunches — which is why the three- and five-factor models exist.

---

*End of practice bank. Re-attempt Section D from memory after a day; if you can also reproduce the three nested forms with their empirical verdicts (C1), the Grossman-Stiglitz paradox (A6), and the joint-hypothesis problem (A7, C-thread) unprompted, the chapter is secure.*
