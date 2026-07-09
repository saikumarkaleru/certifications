# Q&A — Passive vs Active Management

> Scope: Investments — Chapter 17 (Passive vs Active Management). Every question is followed by a full model answer. All rates are annual and in percent unless stated. Work every numerical problem yourself before checking the solution. Sections: **A** concept-check · **B** numerical (full step-by-step, reconciling) · **C** interview-style · **D** MCQs with reasoning.

---

## The chapter in one line

$$\text{Active}_{\text{gross}}=\text{Passive}_{\text{gross}}, \qquad \text{Active}_{\text{net}}<\text{Passive}_{\text{net}}, \qquad \text{Active Share}=\tfrac12\sum_i|w_{f,i}-w_{b,i}|$$

**One-line statement:** Because the market is the sum of its participants, active management is zero-sum before costs and negative-sum after — so passive is the evidence-backed default, and the sophisticated answer is not either/or but a cheap passive core plus deliberate active satellites where inefficiency or genuine skill gives net alpha a fighting chance.

---

## Section A — Concept Check

**A1. State Sharpe's arithmetic of active management and explain why it needs no assumption about market efficiency.**
Sharpe's identity (1991): before costs the average actively managed dollar earns the same as the average passively managed dollar; after costs the active dollar earns *less*. It is accounting, not empirics — passive investors hold the market in market weights, so the *remaining* active holdings must in aggregate also equal the market. Both cohorts earn the same gross return; the active cohort just pays higher fees to do it. No belief about whether prices are "right" is required. This is why the burden of proof sits on active — passive is the default you argue *away* from.

**A2. "Active management is a negative-sum game." Reconcile this with some active funds clearly beating the market every year.**
The claim is about the *aggregate*, not any single fund. Active is zero-sum before costs — every dollar of outperformance is matched by an active dollar of underperformance, because the combined active holdings are just the market — and fees shift the distribution left, making it negative-sum on average. Winners always exist each period; the decisive questions are whether the *cohort* wins (it cannot, by arithmetic) and whether you can identify tomorrow's winners *in advance* (persistence evidence: essentially no).

**A3. Distinguish the three index-replication methods and when each is used.**
*Full replication* holds every constituent in exact weight — for concentrated, liquid indices (S&P 500, Nifty 50); lowest tracking error but costly for broad indices. *Sampling/optimisation* holds a representative subset matched to the index's risk factors — for very broad or illiquid indices; cheaper but adds sampling tracking error. *Synthetic (swap-based)* holds a collateral basket and enters a total-return swap to receive the index return — for hard-to-access markets; low tracking error but adds counterparty risk.

**A4. Explain the ETF creation/redemption mechanism and why it keeps price near NAV.**
Supply is elastic through Authorised Participants (APs) who create and redeem shares in large blocks. At a *premium* to NAV, an AP buys the basket, delivers it in-kind for new ETF shares, and sells those shares — pushing price down. At a *discount*, the AP buys cheap ETF shares, redeems them in-kind for the basket, and sells it — pushing price up. This continuous arbitrage tethers price to NAV via the law of one price.

**A5. Why are ETFs more tax-efficient than traditional mutual funds?**
ETF redemptions settle *in-kind*: the fund hands its lowest-cost-basis shares to a redeeming AP instead of selling for cash, so it never realises a capital gain. A mutual fund must sell holdings for cash to meet redemptions, realising gains distributed to *remaining* shareholders as an unchosen taxable event. The advantage is largest in taxable accounts, widening the passive edge there.

**A6. What does SPIVA measure, why is survivorship-bias correction essential, and what does it show?**
SPIVA scorecards compare active funds against the correct benchmark, counting funds that closed or merged rather than dropping them — essential because dead funds are disproportionately poor, so ignoring them flatters the survivors. Representative findings: ~50–65% of US large-cap active funds lag over 1 year, ~85–90% over 10 years, ~90–95% over 15–20 years. The deterioration with horizon comes from compounding fee drag plus the culling of weak funds, whose survivors still mostly lag.

**A7. What does the persistence evidence add beyond SPIVA, and why is it the "empirical dagger"?**
SPIVA shows most funds lag; persistence asks whether *past winners keep winning*. S&P's Persistence Scorecard repeatedly finds a top-quartile fund is roughly no more likely than chance — often less — to stay top-quartile next period. The dagger: even *if* skilled managers exist, past performance does not reliably identify them ex ante — exactly the information an investor needs to pick a winner.

**A8. Contrast what tracking error means for a passive fund versus an active fund.**
TE is the standard deviation of the fund-minus-benchmark return series. For a *passive* fund it is a quality defect — a good index fund has TE of a few basis points to ~0.20%; high TE means poor replication (fees, cash drag, sampling). Lower is better. For an *active* fund, TE measures how active the manager is — you cannot beat an index you hug, so genuine bets require meaningful TE (say 4–10%). Near-zero TE on an active fund is a red flag.

**A9. Define Active Share and explain how it exposes closet indexing.**
Active Share $=\tfrac12\sum_i|w_{f,i}-w_{b,i}|$, from 0% (pure index) to 100% (no overlap). A *closet indexer* charges active fees (0.8–1.2%) but holds a near-index portfolio (low Active Share, low TE), so the investor gets an expensive index fund and underperforms by roughly the fee. Cremers-Petajisto (2009): funds below ~60% are effectively closet indexers, genuinely active ones sit above ~80%. High Active Share is *necessary* but not *sufficient* for outperformance — it filters out closet indexers, it does not confer skill.

**A10. State the Grossman-Stiglitz paradox and its implication for the passive/active balance.**
If markets were perfectly efficient no one would be paid to gather information, so no one would — and prices would stop reflecting information, making markets inefficient. Hence an equilibrium amount of active management must persist; active managers collectively *make* markets efficient. Implication: passive can never fully "win" — if it grows without bound, price discovery weakens, mispricings widen, and the payoff to active rises, a self-correcting dynamic keeping the two in equilibrium.

**A11. What is the core-satellite approach and its underlying logic?**
It pairs a passive *core* (typically 60–90%) of low-cost broad index funds capturing market beta cheaply with active *satellites* (10–40%) deployed only where the investor has genuine conviction active can add value — inefficient segments, a skilled manager, a factor tilt, or a non-return objective. The logic is a cost/conviction budget: get the market cheaply in the core, and spend your fee budget deliberately on the few bets where expected net alpha justifies the cost — capping active downside to the satellite sleeve while preserving upside.

**A12. Name three conditions under which active management is genuinely defensible.**
(1) *Inefficient segments* — small/micro-cap, emerging and frontier equity, distressed and high-yield credit, private markets — where fewer analysts compete and mispricings survive. (2) *Documented, repeatable skill* — a rare minority whose gross alpha is real, though skill is scarce, hard to separate from luck ex ante, and (Berk-van Binsbergen) tends to be *captured* by the manager in fees. (3) *Non-return objectives* — liability matching, ESG screening, tax-loss harvesting, tail-risk management — where beating the benchmark is not the goal.

---

## Section B — Numerical Problems

**B1. The compounding cost of active fees.** Two investors each invest a $100,000 lump sum for 30 years. The market returns 8% gross annually. Investor P holds a passive fund (expense ratio 0.05%); Investor A holds an *average* active fund charging 0.85% that earns the market's gross return before fees. Net return = gross − expense ratio. Find both terminal wealths and the fee cost.

**Step 1 — Net returns.** P: $8-0.05=7.95\%$. A: $8-0.85=7.15\%$.

**Step 2 — Investor P.** $100{,}000\times(1.0795)^{30}$. $\ln 1.0795=0.076486$; $\times 30=2.29458$; $e^{2.29458}=9.920$. **≈ \$992,000.**

**Step 3 — Investor A.** $100{,}000\times(1.0715)^{30}$. $\ln 1.0715=0.069056$; $\times 30=2.07168$; $e^{2.07168}=7.938$. **≈ \$793,800.**

**Step 4 — Cost & reconcile.** Difference $=992{,}000-793{,}800=\mathbf{\$198{,}200}$: the 0.80% fee gap destroyed ~20% of the passive investor's terminal wealth ($793{,}800/992{,}000=0.800$) *before* any skill deficit. And $793,800 is optimistic — the average active dollar only earns the market gross return, so trading costs push the *median* active outcome lower still.

**B2. Diagnosing a closet indexer from its numbers.** Fund X is benchmarked to the S&P 500, charges 0.90%, has Active Share 35% and TE 1.1%, and returned −0.95% p.a. vs the index over 10 years. Show that its shortfall is consistent with the arithmetic and state the recommendation.

**Solution.** Active Share 35% means 65% of the fund *is* the index, and TE of 1.1% confirms it barely deviates — so it cannot generate enough gross excess return to cover its 0.90% fee. Predicted shortfall ≈ fee + trading cost ≈ 0.90% + 0.05% ≈ 0.95%, matching the observed −0.95% almost exactly. Textbook closet indexer. **Recommendation: replace with a ~0.05% index fund and recover ~0.90%/yr.**

**B3. Computing Active Share.** A three-stock fund holds A 50%, B 30%, C 20%. The benchmark holds A 40%, B 40%, D 20% (the fund holds no D; the benchmark holds no C). Compute Active Share.

**Solution.** Align all four names and take absolute weight differences:
- A: $|0.50-0.40|=0.10$
- B: $|0.30-0.40|=0.10$
- C: $|0.20-0.00|=0.20$
- D: $|0.00-0.20|=0.20$

Sum $=0.60$; Active Share $=\tfrac12(0.60)=\mathbf{30\%}$. **Reconcile:** both weight sets sum to 100%, so overweights equal underweights and the ½ avoids double-counting. At 30% — well below the ~60% threshold — this "active" fund is largely the benchmark.

**B4. Core-satellite blended cost.** A $1,000,000 book: core 75% at a blended 0.07%; satellites — $100,000 EM small-cap active at 1.10%, $80,000 concentrated global manager at 0.95%, $70,000 thematic/private sleeve at 1.20%. Find the blended cost and the maximum drag if every satellite underperforms by 1% net.

**Solution — blended cost.**
$$0.75(0.07\%)+0.10(1.10\%)+0.08(0.95\%)+0.07(1.20\%)$$
$$=0.0525\%+0.110\%+0.076\%+0.084\%=\mathbf{0.3225\%}.$$
A whole-portfolio cost of ~0.32% versus 0.90%+ for an all-active book.

**Bounded downside.** Satellites are 25% of the book, so if each lags by 1% net the drag on the *total* is $0.25\times1\%=\mathbf{0.25\%}$ — the passive core (75%) is untouched by manager risk, fencing the maximum active damage inside the satellite sleeve. That is the point of the architecture.

**B5. Turnover, cost, and the true active handicap.** A passive fund costs 0.10% all-in. An active fund quotes a 0.85% expense ratio but, at 90% turnover, incurs an extra ~0.40% in trading costs, spreads and tax drag not shown in the expense ratio. Against a 4.5% equity risk premium, express the active fund's total handicap.

**Solution.** True active cost $=0.85\%+0.40\%=1.25\%$; handicap vs passive $=1.25\%-0.10\%=\mathbf{1.15\%}$/yr — inside the "1–2% all-in" range. As a share of the 4.5% premium, $1.15/4.5=\mathbf{25.6\%}$: the fund must generate gross alpha equal to over a quarter of the entire equity premium *just to break even*. The visible 0.85% expense ratio understates the true gap by nearly half once turnover is counted — which is why the headline flatters active.

---

## Section C — Interview-Style Questions

**C1. "Why does the average active fund underperform its benchmark?"**
It is structural, not a statement about talent. By Sharpe's arithmetic active investors in aggregate hold the market, so they earn the market's gross return collectively, then pay higher fees, trading costs and taxes to do it — making the *average* active dollar lag the average passive dollar by the cost gap. Compounding turns a ~0.8% annual fee difference into ~20% of terminal wealth over 30 years. It is baked into the accounting before we ask whether any manager has skill.

**C2. "How does an ETF track its index and stay at NAV — and why is that tax-efficient?"**
The fund replicates by full replication, sampling, or a swap; its exchange price stays glued to NAV through Authorised Participants. Above NAV they buy the basket, deliver it in-kind for new ETF shares, and sell those shares, pushing price down; below NAV they buy cheap shares, redeem in-kind for the basket, and sell it, pushing price up. That in-kind redemption is also the tax trick — the fund ships out its lowest-basis lots without selling for cash, so it never realises a gain, unlike a mutual fund that must sell to raise cash and distributes the gain to remaining holders.

**C3. "You don't have to believe in the EMH to prefer passive. Explain."**
Correct — the strong case is Sharpe's arithmetic, an identity independent of efficiency. You need only believe markets are efficient *enough* that the marginal mispricing is too small, rare, or costly to exploit reliably after fees. In large, liquid, researched markets like US large-cap, thousands of analysts compete away obvious mispricings, so net opportunity is thin. Preferring passive is a bet about the *scarcity of net alpha*, not a claim prices are always right.

**C4. "When would you actually recommend active management?"**
Three situations. First, inefficient segments — small/micro-cap, emerging and frontier equity, distressed credit, private markets — where fewer analysts compete and mispricings persist. Second, where there is evidence of genuine activeness and skill (meaningful Active Share and TE, a defensible process), sized as a satellite because skill is hard to identify ex ante. Third, non-return objectives a cap-weighted index cannot serve — liability matching, ESG screening, tax-loss harvesting, tail-risk control. In all cases I'd fence it inside a satellite sleeve, not the core.

**C5. "A client is proud their active fund beat the index last year. How do you respond?"**
Congratulate, then reframe. Some active funds beat the market every year — that is guaranteed by the arithmetic, and one good year is well within luck's range. The decision-relevant question is whether outperformance *persists*, and the Persistence Scorecard shows past top-quartile funds are no more likely than chance to stay there. I'd then check Active Share, TE and fee — genuine bets or closet-indexing beta? — and whether the gain was alpha or simply a factor tilt we could buy more cheaply.

**C6. "What is closet indexing and how do you detect it?"**
A closet indexer charges active fees while holding a near-benchmark portfolio — the investor pays for skill and gets an expensive index fund, guaranteeing underperformance by roughly the fee. Detect it with two numbers: low Active Share (below ~60% means most of the fund *is* the index) and low tracking error (it can't deviate enough to beat its fee). The rule: if you pay active fees, demand evidence of activeness — otherwise replace it with an index fund and pocket the fee.

**C7. "If passive keeps growing, does active eventually make a comeback?"**
In principle yes — Grossman-Stiglitz at market scale. If passive grows without bound, fewer participants do price discovery, mispricings widen, and the payoff to skilled active work rises, drawing capital back; the two coexist in a self-correcting equilibrium. But the systemic argument doesn't tell *you* that *your* chosen active fund will beat its fee today — that the equilibrium amount of active management survives says nothing about whether the marginal fund you can buy is one of the skilled few.

**C8. "Isn't high tracking error a bad thing?"**
It depends on the fund's job. For a passive index fund, yes — high TE means poor replication, and I'd want only a few basis points. For an active fund, near-zero TE is the red flag: you cannot earn alpha from an index you're hugging, so genuine active management *requires* meaningful TE. The right frame is always "whose fund, what objective" — TE is a defect for the replicator and a prerequisite for the stock-picker.

---

## Section D — Multiple-Choice Questions (with reasoning)

**D1. Sharpe's arithmetic of active management depends on which assumption?**
(a) Markets are perfectly efficient · (b) Markets are weak-form efficient · (c) No assumption about efficiency · (d) Managers are irrational
**Answer: (c).** It is an accounting identity — the active cohort's holdings equal the market minus the passive cohort's, so both earn the market gross return regardless of whether prices are "right." (a)/(b) confuse the arithmetic with the separate EMH argument; (d) is irrelevant.

**D2. An ETF is trading at a premium to NAV. What does an Authorised Participant do to arbitrage it?**
(a) Buy ETF shares and redeem them in-kind · (b) Buy the underlying basket, deliver in-kind for new ETF shares, and sell them · (c) Short the basket and buy ETF shares · (d) Do nothing until the discount appears
**Answer: (b).** At a premium the AP creates shares — buys the basket, delivers in-kind for new ETF shares, and sells them, and the selling pushes price back to NAV. (a) describes the *discount* (redemption) case. The premium/discount trigger is the key distinction.

**D3. Which fund is most likely a closet indexer?**
(a) Active Share 88%, TE 8.5%, fee 0.95% · (b) Active Share 35%, TE 1.1%, fee 0.90% · (c) Active Share 72%, TE 4.8%, fee 0.90% · (d) Active Share 5%, TE 0.05%, fee 0.05%
**Answer: (b).** Low Active Share (35%) and low TE (1.1%) combined with a *high active fee* (0.90%) is the closet-indexer signature — index-like holdings at an active price. (d) has the same low activeness but a passive fee, so it *is* an honest index fund, not a closet indexer. (a) and (c) are genuinely active.

**D4. Over a 15–20 year horizon, SPIVA scorecards typically show what fraction of active US large-cap funds underperform the benchmark?**
(a) ~25% · (b) ~50% · (c) ~70% · (d) ~90–95%
**Answer: (d).** Underperformance rises with horizon — ~50–65% over 1 year but ~90–95% over 15–20 years — driven by compounding fee drag and survivorship culling. This is survivorship-bias corrected, so it is not flattered by dropping dead funds.

**D5. ETFs are more tax-efficient than mutual funds primarily because:**
(a) They have lower expense ratios · (b) In-kind redemptions let the fund shed low-basis lots without realising gains · (c) They are exempt from capital-gains tax · (d) They never pay dividends
**Answer: (b).** The in-kind creation/redemption mechanism lets the fund hand low-cost-basis shares to redeeming APs without selling for cash, avoiding realised gains. (a) is sometimes but not always true and isn't the tax reason; (c) and (d) are false — ETFs are taxed and do distribute dividends.

**D6. For an actively managed fund, a tracking error near zero most likely indicates:**
(a) Excellent skill · (b) Low risk and high alpha · (c) Closet indexing · (d) High Active Share
**Answer: (c).** You cannot outperform an index you hug, so near-zero TE on an *active* fund signals it is barely deviating — closet indexing. (d) is the opposite; high Active Share would come with meaningful TE. (a)/(b) invert the logic — zero TE guarantees you cannot add alpha.

**D7. The Grossman-Stiglitz paradox implies that:**
(a) Passive investing will eventually eliminate all active managers · (b) Markets cannot be perfectly efficient because then no one would pay to gather information · (c) Active managers always beat passive · (d) Index funds cause bubbles
**Answer: (b).** If prices already reflected all information, information-gathering would be unpaid and would stop — so some active management must survive to *produce* efficiency, and passive and active coexist in equilibrium. (a) contradicts the paradox; (c) and (d) are not what it states.

**D8. In a core-satellite portfolio, if satellites are 25% of the book and each underperforms by 1% net, the drag on the total portfolio is:**
(a) 1.00% · (b) 0.25% · (c) 0.75% · (d) 0.05%
**Answer: (b).** $0.25\times1\%=0.25\%$. The passive core (75%) is unaffected by manager risk, so active downside is fenced inside the satellite sleeve — the whole point of capping the fee/conviction budget.

**D9. High Active Share (above ~80%) tells you that a fund:**
(a) Will outperform its benchmark · (b) Is taking genuine active bets, which may be right or wrong · (c) Has low fees · (d) Has low tracking error
**Answer: (b).** High Active Share is *necessary* but not *sufficient* for outperformance — it means real deviation, filtering out closet indexers, but the bets can still be wrong. (a) overclaims; (d) is contradicted (activeness raises TE).

**D10. Which is a legitimate reason to choose active management despite the arithmetic?**
(a) Because active funds are cheaper · (b) Because past winners reliably keep winning · (c) In inefficient segments like small-cap and emerging markets, or for non-return objectives like ESG or liability matching · (d) Because index funds carry more market risk
**Answer: (c).** Active is defensible in inefficient segments and for objectives a cap-weighted index cannot serve. (a) is false; (b) is contradicted by persistence evidence; (d) is false — an index fund carries exactly the market's risk, no more.

---

## Self-check

Coverage: **A** 12 concept · **B** 5 worked and reconciled numericals · **C** 8 interview answers · **D** 10 MCQs with distractor reasoning. All figures tie to the source chapter (passive 0.03–0.20% vs active 0.5–1.5%; ~90% underperformance over 15–20yrs; ~20% fee drag over 30yrs; Active Share <60% closet / >80% active; core 60–90%).
