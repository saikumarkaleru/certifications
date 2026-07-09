"""Value-at-Risk analysis for an 8-stock US large-cap portfolio.

Pipeline: fetch data -> compute VaR / ES / component VaR -> backtest ->
write Excel + charts -> print a console summary.

Run from this folder:  python main.py
"""

from __future__ import annotations

import os
import sys

# Make the local src/ package importable regardless of the working directory.
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "src"))

from var_engine import data, var_methods, backtest, reporting  # noqa: E402

INPUT_DIR = os.path.join(HERE, "input")
OUTPUT_DIR = os.path.join(HERE, "output")
CONFIDENCES = [0.95, 0.99]


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    notional = data.PORTFOLIO_NOTIONAL
    weights = data.WEIGHTS
    tickers = data.TICKERS

    # --- 1. Data ---
    prices, source = data.load_price_data(INPUT_DIR, years=2.5)
    returns = data.compute_returns(prices)
    port_ret = data.portfolio_returns(returns, weights)

    # --- 2. Parametric moments (shared by several methods) ---
    mu_p, sigma_p, mean_vec, cov = var_methods.portfolio_moments(returns, weights)

    # --- 3. VaR + ES for each confidence and method ---
    var_summary_rows = []      # for Excel
    var_table = {}             # for console: var_table[conf][method] = (pct, dollars)
    es_table = {}
    for conf in CONFIDENCES:
        h_var = var_methods.historical_var(port_ret, conf)
        p_var = var_methods.parametric_var(mu_p, sigma_p, conf)
        mc_var, _sims = var_methods.monte_carlo_var(mean_vec, cov, weights, conf)

        h_es = var_methods.historical_es(port_ret, conf)
        p_es = var_methods.parametric_es(mu_p, sigma_p, conf)

        var_table[conf] = {
            "Historical": (h_var, h_var * notional),
            "Parametric": (p_var, p_var * notional),
            "MonteCarlo": (mc_var, mc_var * notional),
        }
        es_table[conf] = {
            "Historical": (h_es, h_es * notional),
            "Parametric": (p_es, p_es * notional),
        }

        var_summary_rows.append(["Historical", conf, h_var, h_var * notional, h_es, h_es * notional])
        var_summary_rows.append(["Parametric", conf, p_var, p_var * notional, p_es, p_es * notional])
        var_summary_rows.append(["MonteCarlo", conf, mc_var, mc_var * notional, "", ""])

    # --- 4. Component / marginal VaR (95%) ---
    comp = var_methods.component_var(returns, weights, 0.95, tickers)
    comp_dollars = comp.copy()
    comp_dollars["component_var_$"] = comp_dollars["component_var"] * notional

    # --- 5. Rolling VaR + backtest (95%) ---
    rolling = var_methods.rolling_historical_var(port_ret, window=250, conf=0.95)
    bt = backtest.run_backtest(port_ret, window=250, conf=0.95)

    # --- 6. Reports ---
    xlsx = reporting.write_excel(
        os.path.join(OUTPUT_DIR, "var_analysis.xlsx"),
        returns, var_summary_rows, comp, bt, source, notional,
    )
    png1 = reporting.chart_distribution(
        port_ret, var_table[0.95]["Historical"][0], var_table[0.99]["Historical"][0],
        os.path.join(OUTPUT_DIR, "return_distribution.png"),
    )
    png2 = reporting.chart_rolling_var(rolling, os.path.join(OUTPUT_DIR, "rolling_var.png"))
    png3 = reporting.chart_risk_contribution(comp, os.path.join(OUTPUT_DIR, "risk_contribution.png"))

    # --- 7. Console summary ---
    _print_summary(source, prices, returns, notional, mu_p, sigma_p,
                   var_table, es_table, comp_dollars, bt, [xlsx, png1, png2, png3])


def _print_summary(source, prices, returns, notional, mu_p, sigma_p,
                   var_table, es_table, comp_dollars, bt, files):
    line = "=" * 68
    print(line)
    print("VALUE-AT-RISK ANALYSIS  -  8-stock US large-cap portfolio")
    print(line)
    print(f"Data source     : {source}")
    print(f"History         : {len(returns)} daily returns "
          f"({prices.index[0].date()} -> {prices.index[-1].date()})")
    print(f"Portfolio value : ${notional:,.0f}")
    print(f"Daily mean/vol  : {mu_p:+.4%}  /  {sigma_p:.4%}")
    print()

    print("1-DAY VaR  (loss in $ ; % of portfolio in parentheses)")
    print("-" * 68)
    print(f"{'Confidence':<12}{'Historical':>18}{'Parametric':>18}{'MonteCarlo':>18}")
    for conf in CONFIDENCES:
        row = var_table[conf]

        def fmt(m):
            pct, dol = row[m]
            return f"${dol:,.0f} ({pct:.2%})"

        print(f"{conf:>7.0%}     {fmt('Historical'):>18}{fmt('Parametric'):>18}{fmt('MonteCarlo'):>18}")
    print()

    print("EXPECTED SHORTFALL (CVaR, loss in $)")
    print("-" * 68)
    for conf in CONFIDENCES:
        h = es_table[conf]["Historical"]
        p = es_table[conf]["Parametric"]
        print(f"{conf:>7.0%}     Historical ${h[1]:>10,.0f} ({h[0]:.2%})     "
              f"Parametric ${p[1]:>10,.0f} ({p[0]:.2%})")
    print()

    print("TOP RISK CONTRIBUTORS (parametric component VaR, 95%)")
    print("-" * 68)
    top = comp_dollars.sort_values("component_var", ascending=False).head(4)
    for _, r in top.iterrows():
        print(f"  {r['ticker']:<6} weight {r['weight']:>5.1%}   "
              f"component VaR ${r['component_var_$']:>9,.0f}   "
              f"{r['pct_contribution']:>5.1%} of risk")
    print()

    print("BACKTEST (rolling 250-day historical VaR, 95%)")
    print("-" * 68)
    print(f"  Observations        : {bt.n_obs}")
    print(f"  Exceptions          : {bt.n_exceptions}  (expected {bt.expected:.1f})")
    print(f"  Kupiec POF          : LR={bt.lr_uc:.3f}  p={bt.p_uc:.3f}")
    print(f"  Christoffersen ind. : LR={bt.lr_ind:.3f}  p={bt.p_ind:.3f}")
    print(f"  Conditional cover.  : LR={bt.lr_cc:.3f}  p={bt.p_cc:.3f}")
    print(f"  VERDICT (5% level)  : {bt.verdict()}")
    print()

    print("FILES WRITTEN")
    print("-" * 68)
    for f in files:
        print(f"  {f}")
    print(line)


if __name__ == "__main__":
    main()
