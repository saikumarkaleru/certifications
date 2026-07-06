# Q&A — Oligopoly and Game Theory

A companion practice bank for the concept guide *Oligopoly and Game Theory*. Every question is followed by a full answer: Section A locks the definitions, Section B builds numerical and game-solving fluency, Section C rehearses finance-interview framing, and Section D pressure-tests your reasoning against distractors.

---

## Section A — Concept-Check Questions

**A1. What single feature separates oligopoly from both perfect competition and monopoly, and why does it break the standard toolkit?**

**Strategic interdependence.** With only a handful of large firms, one firm's price or output choice is big enough to move the market, so rivals notice and react — and each firm knows the others are reasoning the same way about it. In perfect competition each firm is too tiny to matter; a monopolist has nobody to react to. Both can be solved with a single demand curve. Oligopoly cannot, because a firm's best action depends on what it *expects rivals to do*, which depends on what they expect it to do. That circular "I think that you think…" reasoning requires **game theory**, not a demand diagram.

**A2. Define the three ingredients of a game.**

- **Players** — the decision-makers (the firms).
- **Strategies** — the actions available (prices, output levels, whether to advertise, collude, or enter).
- **Payoffs** — the profit each player earns for every *combination* of strategies, displayed in a payoff matrix.

**A3. Distinguish a dominant strategy from a Nash equilibrium.**

A **dominant strategy** is an action that is best for a player *no matter what the rival does* — it needs no prediction of the opponent. A **Nash equilibrium** is a weaker, more general idea: a strategy combination where each player's choice is a best *response to the others'*, so nobody gains by unilaterally deviating. If every player has a dominant strategy, that combination is automatically a Nash equilibrium — but most Nash equilibria involve no dominant strategy at all.

**A4. Why is the prisoner's dilemma the "master metaphor" of oligopoly?**

Because it captures the central tension: collectively firms earn most by cooperating (colluding to hold prices high and split monopoly profit), but each individually gains by cheating (cutting price or expanding output to grab share). Defection is the dominant strategy, so the Nash equilibrium is "both cut price" — jointly *worse* than cooperation. Relabel confess/silent as cut/hold and the structure is identical to a duopoly. It explains in one diagram why collusion is unstable and why price wars happen.

**A5. State the Nash-equilibrium ≠ optimal distinction and give the example.**

A Nash equilibrium is a *stable* outcome (no unilateral improvement), **not** an *efficient* one. In the prisoner's dilemma the Nash equilibrium is both players defecting, yet both would be strictly better off cooperating. Stability is not optimality — this is the single most-tested confusion.

**A6. How does repetition rescue cooperation that collapses in a one-shot game?**

In a **repeated game** firms can adopt a **trigger strategy**: cooperate as long as the rival does, but retaliate (cut price, hard, for a long punishment phase) the first time the rival cheats. Cheating now yields a one-time gain but triggers a future of low profits. If firms are patient enough (low discount rate) and the horizon is indefinite, the discounted future loss outweighs the short-run gain, so cooperation becomes a Nash equilibrium of the repeated game. This is the **folk theorem**; **tit-for-tat** is its famous robust strategy.

**A7. List the conditions that make collusion easier to sustain.**

Few firms; homogeneous product; stable demand; high price transparency; high barriers to entry; frequent/repeated interaction; and similar cost structures. Each either makes coordination easier or makes cheating faster to detect and punish.

**A8. Explain the kinked demand curve and what it does and does *not* explain.**

At the prevailing price a firm assumes **asymmetric rival reactions**: if it raises price, rivals won't follow (they steal its customers) so demand is *elastic* above; if it cuts price, rivals *will* follow so demand is *inelastic* below. This kinks the demand curve, producing a **vertical gap in marginal revenue** beneath the kink. Marginal cost can move within that gap without changing the profit-maximising price — hence **sticky prices**. It explains price *rigidity* but **not** how the initial price was set, and Stigler showed the assumed asymmetry isn't empirically robust.

**A9. Differentiate the Cournot, Bertrand, and Stackelberg models.**

- **Cournot** — firms choose *quantity simultaneously*; equilibrium where reaction functions intersect; yields positive profits between monopoly and competition.
- **Bertrand** — firms choose *price simultaneously* with identical products; with just two firms price collapses to marginal cost (the "Bertrand paradox").
- **Stackelberg** — quantity chosen *sequentially*; the leader commits first and gains a **first-mover advantage**.

The takeaway: whether an oligopoly is profitable depends heavily on whether firms compete on price or quantity and whether products are differentiated.

**A10. Distinguish dominant-firm from barometric price leadership.**

Both are legal-ish coordination substitutes for overt collusion. In **dominant-firm** leadership the largest firm sets the price and small "fringe" firms take it as given, with the dominant firm supplying residual demand. In **barometric** leadership the leader isn't necessarily biggest but is the best at reading market conditions; its price changes act as a trusted signal others follow.

---

## Section B — Applied / Numerical Problems (with full solutions)

**B1. Solve the duopoly payoff matrix.** Using the concept guide's Coke–Pepsi matrix — both hold high: (100, 100); one cuts while the other holds: cutter 140, holder 30; both cut: (60, 60) — find each firm's dominant strategy and the Nash equilibrium.

**Solution.** Check Pepsi's best response to each Coke action.
- If **Coke holds high**: Pepsi earns 140 (cut) vs 100 (hold) → cut is better.
- If **Coke cuts**: Pepsi earns 60 (cut) vs 30 (hold) → cut is better.

Cutting is best regardless → **cut is Pepsi's dominant strategy**. By symmetry it is Coke's too. Both play their dominant strategy, so the **Nash equilibrium is (cut, cut) = (60, 60)** — jointly worse than the (100, 100) both could have earned by holding. Classic prisoner's dilemma.

**B2. The patience threshold for collusion.** Two firms earn 100 each per period if both cooperate. Cheating earns 140 this period but triggers permanent reversion to the (60, 60) price-war payoff forever after. Firms discount future profits at rate *r*, valuing a perpetual annuity of X starting next period at X/r. Below what discount rate does cooperation hold?

**Solution.** Compare the two paths from today.

*Cooperate forever:* 100 today + 100/r from next period on.
*Cheat today:* 140 today + 60/r thereafter (punishment forever).

Cooperation is sustained when:
100 + 100/r ≥ 140 + 60/r
→ 100/r − 60/r ≥ 140 − 100
→ 40/r ≥ 40
→ r ≤ 1.

So for any **r ≤ 100%**, cooperation is a Nash equilibrium of the repeated game. Interpretation: unless firms are wildly impatient (or the horizon is about to end), the discounted stream of future cooperative profit dwarfs the one-shot cheating gain. **Patience sustains the cartel** — the folk-theorem result made concrete.

**B3. Cournot duopoly.** Market demand is P = 120 − Q, where Q = q₁ + q₂. Both firms have constant marginal cost of 0. Find each firm's output, market price, and profit at the Cournot–Nash equilibrium.

**Solution.** Firm 1 maximises π₁ = P·q₁ = (120 − q₁ − q₂)·q₁.
Take the derivative and set to zero: 120 − 2q₁ − q₂ = 0 → reaction function q₁ = (120 − q₂)/2.
By symmetry q₂ = (120 − q₁)/2. Solving simultaneously, set q₁ = q₂ = q:
q = (120 − q)/2 → 2q = 120 − q → 3q = 120 → **q = 40 each**.
Total Q = 80, **P = 120 − 80 = 40**.
Profit each = P·q = 40 × 40 = **1,600**.

**B4. Compare against monopoly and competition.** For the same demand P = 120 − Q, MC = 0, find the monopoly and perfectly competitive outcomes and rank all three.

**Solution.**
*Monopoly:* maximise (120 − Q)Q → 120 − 2Q = 0 → Q = 60, P = 60, profit = 3,600.
*Perfect competition:* P = MC = 0 → Q = 120, P = 0, profit = 0.
*Cournot (from B3):* Q = 80, P = 40, combined profit = 3,200.

Ranking confirms Cournot sits **between** the poles: output 60 < 80 < 120, price 60 > 40 > 0, and joint profit 3,600 > 3,200 > 0. Two competing firms produce more and charge less than a monopoly but less and dearer than perfect competition — and their combined 3,200 is below the 3,600 they'd earn by colluding, which is exactly why the temptation to collude exists.

**B5. Kinked demand — the MR gap.** Above the kink demand is P = 100 − Q (for Q < 20); below it demand is steeper, P = 140 − 3Q (for Q > 20). The kink is at Q = 20, P = 80. Show there is a vertical gap in marginal revenue at Q = 20 and explain the consequence.

**Solution.** MR is derived by doubling the slope of each linear segment.
- Upper segment MR = 100 − 2Q. At Q = 20: MR = 100 − 40 = **60**.
- Lower segment MR = 140 − 6Q. At Q = 20: MR = 140 − 120 = **20**.

So MR jumps discontinuously from 60 down to 20 at Q = 20 — a **vertical gap of 40**. Any marginal-cost curve passing *through* that gap (20 ≤ MC ≤ 60) yields the same profit-maximising output (Q = 20) and price (80). Cost can rise or fall within the gap and the firm doesn't change its price → **price stickiness**, exactly as the model claims.

**B6. Herfindahl-Hirschman Index.** Market A: four firms with shares 40, 30, 20, 10. Market B: two firms with 50, 50. Compute the HHI for each and interpret for a merger regulator.

**Solution.** HHI = sum of squared percentage market shares.
- Market A: 40² + 30² + 20² + 10² = 1,600 + 900 + 400 + 100 = **3,000**.
- Market B: 50² + 50² = 2,500 + 2,500 = **5,000**.

Both exceed the US DOJ "highly concentrated" threshold of 2,500, so both are oligopolistic; Market B (a symmetric duopoly) is markedly more concentrated. A regulator (CCI, DOJ, EU) uses the HHI *level* and the *change* a merger would cause to flag anticompetitive risk — a merger that pushes HHI up by more than 100–200 points in an already-concentrated market draws scrutiny.

**B7. Entry deterrence via backward induction.** An incumbent earns 100 as a monopolist. A potential entrant chooses Enter or Stay Out. If it stays out, payoffs are (Entrant 0, Incumbent 100). If it enters, the incumbent then chooses Fight (price war): payoffs (−10, 20), or Accommodate: (40, 50). Solve the sequential game and state whether "I'll fight any entrant" is a credible threat.

**Solution.** Use backward induction from the incumbent's final move. *If entry occurs*, the incumbent compares Fight (20) vs Accommodate (50) → it prefers **Accommodate (50)**. The entrant, anticipating this, compares Enter (getting 40, since accommodation follows) vs Stay Out (0) → it **Enters**. Equilibrium: **Enter, then Accommodate**, payoffs (40, 50).

The threat "I'll fight any entrant" is **not credible**: once entry has happened, fighting (20) is worse for the incumbent than accommodating (50), so a rational entrant ignores the bluff. To make the threat credible the incumbent must *commit* in advance — e.g., build excess capacity so that fighting actually becomes its best response. This is the logic behind capacity pre-emption.

**B8. The advertising prisoner's dilemma.** Coke and Pepsi each choose High or Low ad spend. Both Low: (100, 100). Both High: (80, 80) — ads cancel out but cost money. One High, other Low: advertiser 120, non-advertiser 60. Find the equilibrium and the collective loss.

**Solution.** For each firm, check the best response.
- If rival plays Low: High gives 120 vs Low 100 → High better.
- If rival plays High: High gives 80 vs Low 60 → High better.

**High is dominant for both**, so the Nash equilibrium is (High, High) = **(80, 80)**. Yet (Low, Low) = (100, 100) is jointly better — the industry destroys **20 of profit each (40 total)** on advertising that nets out competitively. Neither dares unilaterally disarm (cutting to Low while the rival stays High drops it to 60). This is why cola giants compete fiercely on advertising rather than price and still can't escape the spend — a real prisoner's dilemma paid for in marketing budgets.

---

## Section C — Interview-Style Questions (with model answers)

**C1. "In one minute, why can't you analyse an oligopoly with a demand curve the way you do a monopoly?"**

Model answer: "Because of strategic interdependence. In monopoly the firm faces the whole market demand curve and nobody reacts to it. In an oligopoly there are only a few large firms, so any one firm's price or output move is big enough to provoke a rival response — and each firm's best move depends on what it expects rivals to do, which depends on what they expect *it* to do. That circular reasoning can't be captured by a static demand curve; you need game theory — payoff matrices, dominant strategies, Nash equilibrium — to find where the firms actually land."

**C2. "Explain the prisoner's dilemma to a non-economist and tell me why it matters for investing."**

Model answer: "Two firms would both make the most money by keeping prices high and splitting the spoils like a shared monopoly. But each is individually tempted to quietly undercut the other to grab market share — and since both think that way, both cut, and both end up worse off than if they'd cooperated. The stable outcome is the bad one. For investing this is everything: it tells you that a concentrated industry's profits are only as durable as the firms' ability to *not* start a price war. When you assess a moat, you're really asking whether this is a disciplined oligopoly that sustains cooperation, or a fragile one one desperate competitor away from a margin-destroying war."

**C3. "If the prisoner's dilemma says cooperation always collapses, why does OPEC exist and why do concentrated industries stay profitable for decades?"**

Model answer: "Because real firms don't play once — they play repeatedly and indefinitely. Repetition lets them punish cheaters: 'hold price high with me, but the day you cheat I cut hard and we both suffer for years.' Cheating then buys a one-time gain against a long tail of lost profit. If firms are patient — value future profits enough — the future loss outweighs the quick gain and cooperation becomes self-enforcing. That's the folk theorem. It's why disciplined oligopolies like aircraft or, until entrants arrive, telecom can sustain fat margins, and why OPEC holds together most of the time. It also tells you the danger sign: a distressed, short-horizon competitor with nothing to lose is the enemy of industry discipline."

**C4. "Walk me through what happened to Indian telecom after 2016 in game-theory terms."**

Model answer: "Before 2016 India had roughly a dozen operators in an uneasy oligopoly holding prices up. Reliance Jio entered with a huge war chest and offered free voice and near-free data — it defected massively and could absorb the losses. That detonated the industry's tacit cooperation: rivals had to match, average revenue per user collapsed, and the sector consolidated to three players, leaving Vodafone Idea financially crippled. For a credit or equity analyst it's the textbook case of a deep-pocketed entrant breaking a repeated-game equilibrium and destroying incumbent margins and bond values. The endgame is equally instructive — once down to three, the survivors began raising tariffs in near-lockstep, tacit collusion re-emerging in a more concentrated structure."

**C5. "How do Porter's Five Forces and Buffett's 'moat' relate to what we just discussed?"**

Model answer: "They're the practitioner's version of oligopoly theory. Porter's forces — rivalry, threat of entry, buyer and supplier power, substitutes — are exactly the variables that determine whether an oligopoly can sustain cooperation and keep prices above cost. Buffett's moat is whatever protects a firm from the price-war outcome of the prisoner's dilemma: high entry barriers, product differentiation, repeated cooperative interaction. So when I judge whether a company can sustain its ROIC, I'm really assessing its industry's oligopoly dynamics — few firms, high barriers, disciplined conduct — and that judgement feeds straight into the sustainable-margin and terminal-growth assumptions of a DCF."

**C6. "Prices in a concentrated industry haven't moved despite rising input costs. Give me two explanations."**

Model answer: "First, the kinked demand curve: firms believe rivals won't follow a price increase but will match a cut, so the marginal-revenue curve has a vertical gap beneath the current price — costs can rise within that gap without changing the profit-maximising price. Second, and more practically, coordination fear: nobody wants to be the one to move first and risk triggering a price war, so an uneasy tacit equilibrium holds prices steady. I'd caveat the kinked-demand story though — Stigler showed rivals often *do* match increases, and it only explains why a price stays put, not how it got there."

**C7. "Why should a macro or commodities analyst care about game theory?"**

Model answer: "Because forecasting a commodity like oil is largely a cartel-cohesion problem, not a supply-demand curve exercise. OPEC+ is a repeated prisoner's dilemma among sovereign producers; whether crude is at 60 or 100 depends on whether members hold their quotas or cheat. March 2020 was a live demonstration — Saudi and Russia failed to agree cuts, both flooded the market, and oil briefly went negative. That's the payoff matrix's 'both defect' cell playing out in real time. Oil prices then feed inflation, central-bank policy, exporter and importer currencies, and shale-producer credit spreads — so cartel game theory is upstream of a huge amount of macro."

---

## Section D — Multiple-Choice Questions (with reasoning)

**D1.** The defining characteristic of oligopoly is:
A. A single seller B. Many tiny price-takers C. Strategic interdependence among a few firms D. A homogeneous product only

**Answer: C.** Oligopoly is defined by a few large, mutually aware firms whose optimal choices depend on rivals' expected reactions. A single seller (A) is monopoly; many price-takers (B) is perfect competition; homogeneity (D) is neither necessary nor sufficient.

**D2.** A dominant strategy is one that:
A. Is best only if the rival cooperates B. Is best regardless of what the rival does C. Maximises joint profit D. Is the same as the Nash equilibrium by definition

**Answer: B.** A dominant strategy is best no matter what rivals do. It is not conditional (A), needn't maximise *joint* profit (C — in the dilemma it minimises it), and while a dominant-strategy profile *is* a Nash equilibrium, the two concepts are not identical (D) — most Nash equilibria involve no dominant strategy.

**D3.** In the prisoner's dilemma, the Nash equilibrium is:
A. Both cooperate — the efficient outcome B. Both defect — jointly worse than cooperating C. One cooperates, one defects D. There is no Nash equilibrium

**Answer: B.** Defection is dominant for both, so both defect — a stable outcome that is jointly *worse* than mutual cooperation. This is the whole point: Nash equilibrium means stable, not optimal (ruling out A).

**D4.** Cooperation can be sustained in a prisoner's dilemma when the game is:
A. Played once B. Played a known finite number of times C. Repeated indefinitely with patient players D. Played with a dominant strategy to cheat

**Answer: C.** Indefinite repetition plus patient firms lets trigger/tit-for-tat punishment make cooperation a Nash equilibrium (the folk theorem). A one-shot game (A) collapses; a *known* finite game unravels by backward induction from the last round (B).

**D5.** The kinked demand curve model primarily explains:
A. How the initial price is set B. Why oligopoly prices are sticky C. Why cartels always collapse D. First-mover advantage

**Answer: B.** The kink creates a vertical MR gap, so cost changes within the gap leave price unchanged — explaining price rigidity. It explicitly does *not* explain how the prevailing price was set (A) — a known weakness.

**D6.** Under the assumptions of the kinked demand curve, if a firm raises its price, rivals will:
A. Match the increase B. Not follow, so the firm loses many customers C. Also exit the market D. Cut price to match

**Answer: B.** The model assumes rivals ignore price increases (leaving demand elastic above the kink) but match price cuts (inelastic below). A raising firm therefore loses many sales.

**D7.** In a two-firm Bertrand model with identical products, price is driven to:
A. The monopoly level B. Marginal cost C. Above the Cournot price D. Zero output

**Answer: B.** With identical products and price competition, each firm undercuts the other until price equals marginal cost — the "Bertrand paradox." This contrasts sharply with Cournot, where two firms earn positive profit (ruling out A and C).

**D8.** As the number of firms in a Cournot market rises, total output and price move:
A. Output falls, price rises B. Output rises toward the competitive level, price falls toward MC C. Both stay at the monopoly level D. Output rises, price rises

**Answer: B.** More Cournot competitors push total output up toward the competitive quantity and price down toward marginal cost — the model bridges monopoly and perfect competition.

**D9.** Which market condition makes collusion *harder* to sustain?
A. Few firms B. High price transparency C. Frequent repeated interaction D. A desperate, short-horizoned competitor

**Answer: D.** A distressed firm with a short horizon discounts future punishment heavily, so it has little to lose from cheating — it destroys industry discipline. Few firms (A), transparency (B), and frequent interaction (C) all make cooperation *easier* by aiding coordination or swift punishment.

**D10.** An incumbent threatens to start a price war against any entrant, but fighting would leave it worse off than accommodating once entry occurs. Backward induction says the entrant will:
A. Stay out, fearing the war B. Enter, because the threat is not credible C. Enter only if it is larger than the incumbent D. Never enter under any circumstances

**Answer: B.** Since fighting is not the incumbent's best response after entry, the threat is a non-credible bluff; a rational entrant enters and the incumbent accommodates. Making the threat credible requires a prior *commitment* (e.g., excess capacity), which changes the incumbent's post-entry payoffs.

**D11.** The Herfindahl-Hirschman Index (HHI) is used by regulators to:
A. Forecast interest rates B. Measure market concentration and screen mergers C. Set price ceilings D. Compute a firm's marginal cost

**Answer: B.** The HHI sums squared market shares to gauge concentration; competition authorities use its level and the change from a merger to flag anticompetitive risk. It has nothing to do with rates (A), price controls (C), or cost estimation (D).

**D12.** "Barometric" price leadership means the price leader is:
A. Always the largest firm B. The firm best at reading market conditions, whose changes others trust C. Appointed by the regulator D. The lowest-cost producer by law

**Answer: B.** A barometric leader signals price changes based on superior reading of demand and costs, and rivals follow because they trust the signal. The *largest* firm setting price (A) describes *dominant-firm* leadership, a different variant.

---

*End of practice bank. Cross-reference the concept guide's sections on the prisoner's dilemma, the repeated-game escape hatch, and the finance link to moats and DCF terminal value to cement why oligopoly — a prisoner's dilemma played by patient firms — is the theory behind the durability of corporate profit.*
