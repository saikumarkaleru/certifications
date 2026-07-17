# Markov Regime-Switching

The previous chapter classified regimes with thresholds and clustering — useful, but every one of those methods answers only "what regime are we in *now*?" A **Markov regime-switching model** answers two harder and more valuable questions at once: "what is the *probability* we are in each regime right now, given all the evidence?" and "given today's regime, what are the odds we *switch* tomorrow?" It is the formal, probabilistic engine underneath serious regime work — the model James Hamilton introduced to economics in 1989 to describe how GDP flips between expansion and recession, and which now runs on trading desks to model how volatility flips between calm and stress. This chapter builds it precisely, fits it to Nifty, and shows how to turn its outputs into position sizing — while being blunt about the ways it can mislead you.

## The concept

Picture the market as being in one of a few **hidden states** — say State 1 = "calm/bull" and State 2 = "turbulent/bear." You never observe the state directly. You only observe returns. But each state *generates* returns from its own distribution: the calm state produces small returns with low variance and a slight positive drift; the turbulent state produces large, negatively-skewed returns with high variance. From a stream of returns, the model *infers* which state was probably active when.

Two ingredients define it:

1. **State-conditional distributions.** Each regime k has its own parameters — mean μ_k and volatility σ_k (and optionally more). Returns are drawn from N(μ_k, σ_k²) when the market is in regime k.
2. **A Markov transition process.** The regime tomorrow depends *only* on the regime today (the "Markov" memoryless property), governed by a **transition matrix** P. Regimes are *sticky*: the probability of staying is high, of switching is low. That stickiness is exactly the volatility-clustering fact from the last chapter, now written as maths.

The "hidden state + observations" structure makes this a **Hidden Markov Model (HMM)**. Markov regime-switching is the HMM applied to financial returns with Gaussian (or Student-t) emissions.

Why this beats a threshold rule: a threshold gives you a hard, brittle yes/no ("VIX>18 → stress"). The HMM gives you a *smoothed probability* — "78% chance we're in the stress regime" — that fuses *all* the return evidence coherently and updates gracefully. And it hands you the transition matrix, so you can reason about *persistence*: a regime with 98% daily self-transition lasts on average 50 days; one with 90% lasts only 10. You size and plan differently for each.

## The method and the maths

### The transition matrix

For two states, the transition matrix is:

|  | to State 1 | to State 2 |
|---|---|---|
| **from State 1** | p₁₁ | p₁₂ = 1 − p₁₁ |
| **from State 2** | p₂₁ = 1 − p₂₂ | p₂₂ |

Each row sums to 1. A typical fitted equity result looks like p₁₁ = 0.97 (calm is sticky), p₂₂ = 0.92 (stress is sticky but a bit less so, and mean-reverts back to calm). The **expected duration** of a regime is 1/(1 − p_kk): calm lasts 1/(1−0.97) ≈ 33 days; stress lasts 1/(1−0.92) ≈ 12.5 days. This asymmetry — long calms, sharp short stresses — matches real markets and is one of the model's most useful outputs.

### The emission distributions

State 1 (calm): r_t ~ N(μ₁, σ₁²), e.g. μ₁ = +0.05%/day, σ₁ = 0.7%/day.
State 2 (stress): r_t ~ N(μ₂, σ₂²), e.g. μ₂ = −0.15%/day, σ₂ = 2.2%/day.

Fat tails matter, so practitioners often replace the Gaussian with a **Student-t** emission to stop a single crash day from being misclassified as its own regime.

### Fitting: the EM / Baum-Welch algorithm

You don't know the states, the emission parameters, *or* the transition matrix — you infer all of them from returns by maximum likelihood, via the **Expectation-Maximisation** loop (the Baum-Welch algorithm for HMMs):

1. **E-step:** given current parameter guesses, use the **forward-backward algorithm** to compute, for each day, the probability it was in each state (the "smoothed" state probabilities).
2. **M-step:** given those state probabilities, re-estimate μ_k, σ_k and the transition matrix P (weighted averages).
3. Repeat until the likelihood stops improving.

For live, one-sided inference you use only the **filtered probability** — the forward pass using data *up to and including today*, P(state_t = k | data up to t). This is causal and tradeable. The **smoothed probability** uses the whole sample (past *and future*) and is only for backtesting/analysis — using it live is look-ahead bias, one of the most common and fatal errors people make with this model.

### The Viterbi path

If you want a single most-likely *sequence* of hidden states over history (rather than per-day probabilities), the **Viterbi algorithm** decodes it. Handy for labelling a chart's regimes for study; not what you trade on tick by tick.

## Worked India example (levels and ₹)

Fit a 2-state Gaussian regime-switching model to daily Nifty log returns over a multi-year window spanning both quiet grinds and shock episodes. A representative fitted result:

| Parameter | State 1 (calm/bull) | State 2 (turbulent/bear) |
|---|---|---|
| Mean μ (daily) | +0.06% | −0.18% |
| Vol σ (daily) | 0.68% (~10.8% ann.) | 2.15% (~34% ann.) |
| Self-transition p_kk | 0.975 | 0.915 |
| Expected duration | ~40 days | ~12 days |
| Unconditional time in state | ~78% | ~22% |

Read this like a market historian: Nifty spends roughly three-quarters of its life in a calm, gently-rising regime with ~11% annualised vol, punctuated by shorter (~two-week average) turbulent regimes at ~34% annualised vol and negative drift. That *is* the character of Indian equities — long grinds up, sharp scares down.

Now run it live. Suppose the filtered probability of State 2 (turbulence) sits near 5% for weeks while Nifty climbs from 23,000 to 24,500 — the model is confidently in calm-bull. Then a global risk event hits; over two sessions the model's State-2 probability jumps 8% → 35% → 74% as it ingests two wide down-days. The model has *inferred* a regime switch from the return evidence, and — because it knows p₂₂ = 0.915 — it also tells you this turbulence is likely to persist ~12 days, not blow over by tomorrow. That persistence estimate is something no threshold indicator gives you.

**Rupee frame with probability-scaled sizing.** Say your maximum swing position is four Nifty futures lots (lot 75). You size *proportional to the calm-regime probability*: exposure = max_lots × P(calm). 
- Calm phase, P(calm) = 0.95 → hold ~4 lots (round to 4).
- Transition, P(calm) drops to 0.65 → cut to ~3 lots.
- Confirmed turbulence, P(calm) = 0.26 → hold ~1 lot or flat.

If the turbulent regime then delivers the ~500-point Nifty drop the model expected, having scaled from 4 lots to 1 *before* the worst of it saves roughly 500 × 75 × 3 lots-not-held = **₹1,12,500** of drawdown versus a static full-size book. That smooth, probability-weighted de-risking — rather than a jarring all-in/all-out flip — is the practical payoff of the model over a hard threshold.

**Options overlay.** The regime's σ estimate maps directly to options posture. In State 1 (σ ≈ 0.7%/day, low IV), theta-selling — Bank Nifty/Nifty short straddles and iron condors — is in its happy regime. When filtered P(State 2) crosses ~0.5, the model is warning that realised vol is regime-shifting up; a premium-selling book should be reduced or hedged *before* IV fully expands, because State 2's 2.15% daily σ is precisely the environment that detonates naked short-vol positions.

## How to use it in a real TA workflow

1. **Fit offline, run online.** Estimate parameters on a long history (EM/Baum-Welch), then each day compute only the *filtered* state probability from data up to today. Refit periodically (e.g. quarterly) so parameters track the current era — but never so often that they chase noise.

2. **Choose the number of states deliberately.** Two states (calm/turbulent) is robust and interpretable and usually enough. Three (bull/range/bear) can add value but is harder to fit stably. Beyond three or four, the model overfits and states lose meaning. Use BIC/AIC to compare, but weight interpretability heavily.

3. **Translate probability into action.**
   - **Sizing:** position ∝ P(favourable regime), as in the worked example — smooth scaling beats binary switching.
   - **Strategy routing:** high P(calm-trend) → momentum/breakout; high P(turbulent) → defence, hedges, or vol-selling only if it's a *high-IV mean-reverting* turbulent state you've explicitly modelled.
   - **Options:** map state σ to IV posture — sell premium in low-σ states, buy protection or stand aside in high-σ states.

4. **Combine, don't replace.** Use the HMM probability as *one high-quality input* alongside price structure, the composite regime score, and the Hurst read. When the HMM's filtered probability, VIX, and the MA stack all agree on "stress," conviction (and de-risking) is warranted. When they disagree, the market is genuinely in transition — reduce size and wait.

5. **Confluence with the prior two chapters.** Hurst tells you the *texture* (trend vs mean-revert); the composite score gives a transparent cross-check; the HMM adds *calibrated probability and expected persistence*. Together they form a layered regime engine where each method covers another's blind spot.

### Compact fitting snippet

```python
import numpy as np, pandas as pd
from hmmlearn.hmm import GaussianHMM   # pip install hmmlearn

r = np.log(df.close).diff().dropna().values.reshape(-1, 1)  # daily log returns

model = GaussianHMM(n_components=2, covariance_type='diag',
                    n_iter=500, random_state=42).fit(r)

# identify which hidden state is the 'turbulent' one = higher variance
var = model.covars_.ravel()
turbulent = int(np.argmax(var))

# FILTERED (causal) probability of turbulence, usable live
# score_samples gives posterior over ALL data (smoothed) -> for backtest only.
# For a causal read, re-run predict_proba on an expanding window in practice.
post = model.predict_proba(r)
p_turb_today = post[-1, turbulent]

print("Transition matrix:\n", np.round(model.transmat_, 3))
print("State means (daily):", np.round(model.means_.ravel(), 5))
print("State vols  (daily):", np.round(np.sqrt(var), 5))
print(f"P(turbulent today) = {p_turb_today:.2f}")
print(f"Expected turbulent duration = {1/(1-model.transmat_[turbulent,turbulent]):.0f} days")
```

The comment flags the critical trap: `hmmlearn`'s `predict_proba` on the full array returns *smoothed* probabilities that peek at future data. For an honest live signal you must run inference on an expanding window (data only up to each decision day) or use the forward filter explicitly. Backtests that skip this look spectacular and are worthless.

## Honest limitations

**Look-ahead bias is the number-one killer.** Smoothed probabilities use future data; they will make any backtest glow. Only filtered/expanding-window probabilities are tradeable. If a regime backtest looks too clean, you almost certainly leaked the future.

**It still lags at turns.** The model needs a few return observations to shift its probability. It will not call the exact top or bottom — it confirms the switch *after* it starts, just like every detector. Its edge is calibrated confidence and persistence estimates, not clairvoyance.

**Parameter instability and regime relabelling.** Re-fit on a new window and the states can swap indices, drift, or occasionally collapse. You must re-identify which state is which (by variance, as in the snippet) every fit, and check parameter stability. Unstable fits mean an unstable signal.

**The Markov assumption is a simplification.** Real regime durations aren't exactly geometric, and tomorrow depends on more than just today's state (there's longer memory the model ignores). It's a useful caricature, not the truth. Gaussian emissions also understate crash tails — use Student-t if tails matter.

**Small-sample and rare-regime problems.** True crisis regimes (2008, March 2020) are rare, so the model has few examples to learn their parameters, making the high-stress state the least reliably estimated — exactly when you most need it. On the NSE, expiry gaps and event days can also spawn spurious one-off "states" if you over-parameterise.

**It is a classifier, not an alpha source.** Like all regime methods, the HMM only tells you which world you're in. It multiplies the edge of a sound per-regime playbook; it invents no edge on its own. A brilliant regime model wrapped around a losing strategy still loses.

## Interview-ready summary

A **Markov regime-switching model** treats the market as moving between a few **hidden states** (e.g. calm/bull vs turbulent/bear), each generating returns from its own distribution — low-vol slight-positive-drift in calm, high-vol negative-drift in stress — with switches governed by a **transition matrix** whose high self-transition probabilities encode volatility clustering. It's a Hidden Markov Model with Gaussian (or Student-t) emissions, fitted by **EM/Baum-Welch**, and its key outputs are the **filtered probability** of each regime today (causal, tradeable) and the **expected regime duration** 1/(1−p_kk). On Nifty a typical 2-state fit shows ~78% of time in a ~11%-vol calm regime lasting ~40 days and ~22% in a ~34%-vol turbulent regime lasting ~12 days — the long-grind-up, sharp-scare-down character of Indian equities. You trade it by **scaling position size to the favourable-regime probability** (e.g. 4 lots at P(calm)=0.95 down to 1 lot at P(calm)=0.26, potentially saving ₹1,00,000+ of drawdown on a multi-lot Nifty book), routing strategies (momentum in calm, defence/hedges in stress), and mapping state σ to options posture (sell premium in low-σ states, buy protection in high-σ). It beats threshold rules by giving *smoothed, calibrated probabilities and persistence estimates* rather than brittle yes/no flags. Honest limits: it **lags at turns**, its parameters are **unstable** and must be re-identified each fit, the Markov and Gaussian assumptions are simplifications that understate memory and crash tails, rare crisis states are **poorly estimated**, and — decisively — using smoothed (future-peeking) probabilities live is **look-ahead bias** that fakes brilliant backtests. Use only filtered/expanding-window probabilities, combine it with Hurst and a transparent composite score, and remember it classifies the world without creating edge on its own.
