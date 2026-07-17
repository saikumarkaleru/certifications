# Classification Models for Trade Signals

## The concept: predict direction, not price

The single most important reframing in quantitative TA is this: **stop trying to predict the price, and start trying to classify the setup.** Instead of asking "what will Nifty close at next Friday?" — a near-impossible regression problem — you ask "given today's technical state, is the next move more likely up, down, or nothing worth trading?" That is a **classification** problem, and it maps far more naturally onto how a discretionary trader actually thinks. A trader never says "Bank Nifty will be 51,847." A trader says "this looks like a long." Classification models formalise exactly that judgement.

Classification also plays to machine learning's strengths. Directional accuracy of 53–57% — utterly useless as a price forecast — can be a genuinely profitable *edge* if position sizing and risk management are sound, because you are betting on a probability tilt, not a point estimate. The whole game becomes: build a model that outputs a calibrated probability of "up", then act only when that probability is high enough to overcome costs, and size the bet to the confidence.

This chapter covers the models (logistic regression through gradient-boosted trees), the crucial and easily-botched step of **labelling**, evaluation that respects trading reality, and an honest India-first worked example. We build directly on the feature-engineering discipline of the previous chapter — clean, stationary, leak-free features are assumed here.

## Labelling: the decision that makes or breaks everything

A classification model learns to map features → labels. If your labels are naive, the model learns to predict noise no matter how good the features are. Labelling is where most retail ML quietly fails.

**Naive labelling (the one to avoid as default):** label bar *t* as `1` if the next bar's close is higher, else `0`. Problems: (1) it ignores magnitude — a +0.02% grind and a +2% breakout get the same label; (2) it ignores the *path* — price might rally then reverse hard; (3) most 1-bar moves are noise, so ~50% of labels are essentially coin flips, and the model learns nothing separable.

**Threshold labelling:** label `1` only if forward N-day return exceeds a threshold, `−1` if below negative threshold, `0` (no-trade) otherwise. This creates a cleaner three-class problem and — importantly — a "do nothing" class, which matches reality: most days there is no edge.

**The triple-barrier method (López de Prado)** — the professional standard. For each entry candidate, set three barriers before you know the outcome:
- an **upper barrier** (profit target), e.g. +1.5× ATR,
- a **lower barrier** (stop loss), e.g. −1.0× ATR,
- a **vertical barrier** (max holding time), e.g. 10 bars.

Whichever barrier is touched *first* determines the label: hit the top first → `+1` (a "win"), hit the bottom first → `−1` (a "loss"), time out → `0` (or label by sign of return at expiry). This is superb because it labels according to the *actual trade you would take*, respects path dependency, and encodes your real stop/target geometry. On Indian instruments where intraday whips are violent (Bank Nifty routinely travels ±1% before settling), the triple-barrier label captures "would this trade have stopped out?" — which naive labels completely miss.

A refinement, **meta-labelling**: use a primary model or simple rule to decide *direction*, then train a secondary classifier to decide *whether to take* that signal (bet / no-bet). This separates "which way" from "how confident", improves precision, and is one of the more practical ideas for retail — you keep your existing TA setup as the primary signal and let ML act as a filter that says "yes, this instance of your setup looks like the good ones."

## The models — from simple to powerful

**Logistic regression.** Despite the name, a classifier. It models `P(up) = 1 / (1 + e^{−(β₀ + β₁x₁ + … )})`. Linear in the features, outputs a probability, fast, interpretable — you can read the coefficients and know which feature pushes the odds up. It is the correct *first* model. If logistic regression on your features can't beat a coin, a neural net probably won't rescue you; it will just overfit more elegantly. Regularise it (L1/L2) to handle collinear TA features.

**k-Nearest Neighbours.** "Find the 20 most similar historical bars; how did they resolve?" Intuitive — it's literally analogical reasoning, which is what pattern traders do — but sensitive to scaling and the curse of dimensionality, and slow at scale. Useful as a concept check.

**Decision tree.** Splits the feature space with if-then rules ("if RSI < 30 and z-score < −2 and VIX > 18 → up"). Highly interpretable, but a single tree overfits badly.

**Random forest.** An ensemble of many decision trees, each on a bootstrap sample and a random feature subset; predictions are averaged (bagged). Dramatically reduces overfitting versus a single tree, handles non-linear interactions, needs no feature scaling, and gives feature importances. A strong, robust default for tabular TA data.

**Gradient boosting (XGBoost, LightGBM, CatBoost).** Trees built sequentially, each correcting the previous ones' errors. Usually the *best-performing* family on tabular data of the size we have, and it is what most quant desks and Kaggle winners reach for. LightGBM is fast and handles categoricals (like the OI quadrant) well. The cost is more hyperparameters and a greater tendency to overfit small financial datasets if you're not disciplined with regularisation (max_depth, min_child_weight, subsample, learning rate) and early stopping.

**Support Vector Machines** and **shallow neural nets** exist too, but for tabular technical features on modest Indian datasets they rarely beat a well-tuned gradient-boosted tree, and they are harder to reason about. Prefer trees for tabular; save neural nets for when you have genuinely large, structured (e.g. tick-level) data.

## Class imbalance and the "no-trade" majority

With sensible labelling, most bars are `0` (no edge). A model that predicts "no-trade" every time can be 85% "accurate" and utterly worthless. This is **class imbalance**, and accuracy is a trap metric here.

Handle it by: using class weights (penalise mistakes on the rare class more), resampling (SMOTE for the minority class, or undersampling the majority — carefully, respecting time order), and — most importantly — **choosing the right evaluation metric.**

## Evaluation that respects trading reality

- **Confusion matrix** — the base object: true/false positives and negatives.
- **Precision** = of the trades the model said "take", what fraction won. This is what your P&L cares about most — a false positive is a losing trade.
- **Recall** = of all the real opportunities, what fraction the model caught. Missing trades costs opportunity, not capital.
- **F1** = harmonic mean of precision and recall.
- **ROC-AUC / PR-AUC** — threshold-independent ranking quality; PR-AUC is better under imbalance.
- **Probability calibration** — if the model says 70%, do those cases actually win ~70% of the time? Check a calibration/reliability plot; use Platt scaling or isotonic regression to fix miscalibration. Calibration matters because your *sizing* depends on the probability being honest.

But none of these are the real test. **The real test is a walk-forward backtest with costs.** Convert probabilities into positions, apply realistic Indian costs, and look at the equity curve, Sharpe, max drawdown, and hit-rate. A model with mediocre F1 but good calibration at the extreme probabilities can be very profitable if you only trade the high-confidence tail.

**Realistic Indian costs to bake in:** brokerage (₹20/order flat at discount brokers, or zero on equity delivery at some), STT (0.1% on delivery equity buy+sell; 0.02% on the sell side of intraday; 0.1% on F&O option sell premium; 0.02% on futures sell), exchange transaction charges, GST (18% on brokerage + txn charges), SEBI charges, stamp duty, and — the big silent killer — **slippage and the bid-ask spread**, which on mid-caps and far strikes can dwarf everything else. A model showing 0.15% edge per trade before costs is dead on arrival when round-trip friction is 0.10–0.20%.

## Cross-validation for time series — do not shuffle

Standard k-fold cross-validation randomly shuffles rows. **For markets this is catastrophic** — it trains on future data to predict the past, the ultimate leak. Use instead:

- **Walk-forward / expanding window:** train on 2016–2020, test 2021; train 2016–2021, test 2022; and so on. This mimics live deployment.
- **Purged K-Fold with embargo** (López de Prado): when labels span multiple bars (triple-barrier), purge training samples whose label windows overlap the test set, and add an embargo gap so no information bleeds across the boundary.

The discipline: your validation scheme must never let the model see anything it couldn't have seen live. If a result seems too good, the CV is usually leaking.

## Worked India example: a Bank Nifty swing filter with meta-labelling

**Setup.** Primary rule: a simple, well-known long trigger — Bank Nifty closes above its 20-DMA *and* RSI(14) crosses above 55. On its own, over 2016–2023 daily data, suppose this fires ~180 times and wins ~48% with a barely-positive expectancy after costs — a typical "looks good on the chart, breaks even in reality" TA rule.

**Meta-label it.** For every instance where the primary rule fired, apply a triple-barrier label: upper = +1.5×ATR14, lower = −1.0×ATR14, vertical = 10 sessions. That produces a clean win/loss label *for the trades you would actually take*. Now train a LightGBM classifier on the feature set from the previous chapter (distance from SMA50, z-score, ATR%, realised vol, VIX level and change, OI quadrant, days-to-expiry, day-of-week) to predict **P(this firing is a winner)**.

**Result (illustrative, the shape of a realistic outcome).** Train 2016–2021, test 2022–2023 walk-forward. The meta-model's calibrated probability lets you keep only firings with P(win) ≥ 0.60. That filter takes maybe 70 of the 180 signals. On the test slice, filtered precision rises from ~48% to ~58%, and — because you skipped the low-VIX, near-expiry, over-extended firings the model learned to distrust — post-cost expectancy per trade turns clearly positive, Sharpe improves, and max drawdown shrinks because the worst clusters of losers (choppy, high-VIX-collapse regimes) are avoided. Crucially, the model did **not** invent a signal; it *filtered* a known one. That is the realistic, honest way ML helps a TA workflow.

The feature importances tell a readable story: `dist_from_sma50` and `zscore` (avoid buying when already stretched), `vix_change` (falling VIX favours the long), `days_to_expiry` (skip the gamma-whip zone) dominate. Because you can read them, you can sanity-check — and override — the model. That interpretability is worth more than a couple of points of AUC.

## Minimal code sketch

```python
import lightgbm as lgb
from sklearn.metrics import precision_score, classification_report

# X: engineered features on primary-rule firings (already shift(1)-ed)
# y: triple-barrier win(1)/loss(0) labels for those firings
# Chronological split — NEVER shuffle
cut = X.index < '2022-01-01'
X_tr, X_te = X[cut], X[~cut]
y_tr, y_te = y[cut], y[~cut]

model = lgb.LGBMClassifier(
    n_estimators=400, learning_rate=0.03, max_depth=4,
    num_leaves=15, subsample=0.8, colsample_bytree=0.8,
    min_child_samples=30, class_weight='balanced', random_state=42)

model.fit(X_tr, y_tr,
          eval_set=[(X_te, y_te)],
          eval_metric='auc',
          callbacks=[lgb.early_stopping(40)])

proba = model.predict_proba(X_te)[:, 1]
take  = proba >= 0.60                      # trade only high-confidence
print("filtered precision:",
      precision_score(y_te[take], (proba[take] >= 0.60).astype(int)))
# Then: feed `take` into a walk-forward backtest WITH Indian costs.
```

The `max_depth=4`, `min_child_samples=30` and early stopping are deliberate — small financial datasets demand shallow, regularised trees. The `class_weight='balanced'` handles the win/loss imbalance. And the threshold 0.60 is not sacred; you tune it on validation to trade off frequency versus precision, then confirm on a truly held-out slice.

## How to use it in a real trading workflow

1. Keep your discretionary/rule-based TA as the **primary** signal generator.
2. Let the classifier act as a **filter and sizer**: skip low-probability firings; size larger when P(win) is high (fractional-Kelly on the calibrated probability, capped).
3. Retrain on a schedule (e.g. quarterly) with an expanding window; markets drift.
4. Monitor live precision vs backtest precision. A sustained gap means regime change or leakage — pause and investigate.
5. Never remove the human circuit-breaker. Around events (RBI policy, Budget, election counting, global shocks) the model is extrapolating outside its training distribution; those are the days to stand down or halve size.

## Pitfalls

- **Naive 1-bar labels** — mostly noise; use threshold or triple-barrier.
- **Accuracy on imbalanced classes** — meaningless; use precision/PR-AUC and, ultimately, a cost-aware backtest.
- **Shuffled cross-validation** — leaks the future; use walk-forward / purged K-fold with embargo.
- **Ignoring costs and slippage** — the number-one reason paper edges vanish on NSE, especially in options and mid-caps.
- **Overfitting via deep trees / too many features on small data** — regularise hard, keep features few.
- **Uncalibrated probabilities** driving position size — calibrate before you size.
- **Trusting a black box on event days** — the model has never seen this regime.
- **Data-snooping across many model/threshold trials** — every extra experiment on the same test set inflates false discovery; keep a final, untouched hold-out.

## Interview-ready summary

Classification reframes TA-ML from the near-impossible ("what price?") to the tractable and trade-relevant ("is this setup likely to work?"). The most consequential step is labelling: avoid naive next-bar labels and use threshold or, better, the triple-barrier method, which labels each candidate by which of profit-target / stop / time-out is hit first — matching the trade you'd actually take. Meta-labelling (let ML decide bet/no-bet on a known signal) is the most practical retail pattern. Prefer interpretable models first — logistic regression, then random forest, then gradient-boosted trees (LightGBM/XGBoost), which usually win on tabular data of this size. Because the "no-trade" class dominates, judge the model by precision, PR-AUC and probability calibration — never plain accuracy — and above all by a walk-forward backtest with full Indian costs (STT, GST, transaction charges, and slippage). Validate only with time-aware schemes (walk-forward, purged K-fold with embargo); shuffled CV leaks the future. Used honestly, ML rarely invents signals — it filters and sizes the ones you already have, and its greatest value is telling you when *not* to trade.
