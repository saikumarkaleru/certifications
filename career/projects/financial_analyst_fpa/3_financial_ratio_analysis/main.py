"""
Financial Ratio Analysis + DuPont + Peer Benchmarking
=====================================================

One command -> a full analyst's read on a company and how it compares to peers.

Pipeline (each step lives in its own module under src/ratios/):
  1. LOAD    real financials for a TARGET (AAPL) and PEERS (MSFT, GOOGL, AMZN,
             META) via yfinance -- cached to input/ so reruns are offline, with
             a bundled illustrative fallback so this ALWAYS runs.        [data]
  2. RATIOS  the four families (profitability, liquidity, leverage,
             efficiency) over several years.                          [ratios]
  3. DUPONT  break the latest ROE into its 3-step and 5-step drivers.  [dupont]
  4. BENCH   percentile-rank the target against peers on each key ratio.[benchmark]
  5. TRENDS  flag each target ratio Improving / Deteriorating / Flat.  [quality]
  6. FLAGS   earnings-quality red-flag panel (accruals, cash conversion).[quality]
  7. REPORT  print a console summary, then write Excel + PNG charts. [reporting]

Run:  python main.py
"""

from __future__ import annotations

import os
import sys

# Make the src/ package importable no matter where we are launched from.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

from ratios import data, ratios as ratio_mod, dupont, benchmark, quality, reporting


def main():
    target = data.TARGET
    peers = data.PEERS

    # -- 1. LOAD -------------------------------------------------------------
    facts_by_ticker, source = data.load_all()
    tfacts = facts_by_ticker[target]
    latest = ratio_mod.latest_year(tfacts)

    print("\n" + "=" * 70)
    print(" FINANCIAL RATIO ANALYSIS  +  DuPont  +  PEER BENCHMARKING")
    print("=" * 70)
    print(f" Target: {target}   Peers: {', '.join(peers)}")
    print(f" Data source: {source.upper()}   Latest fiscal year: {latest}")

    # -- 2. RATIOS -----------------------------------------------------------
    r = ratio_mod.compute_ratios(tfacts)
    print("\n--- KEY RATIOS (target, most recent year) ---")
    latest_col = r[latest]
    for name in ratio_mod.KEY_RATIOS:
        val = latest_col.get(name, float("nan"))
        print(f"   {name:<32} {val:>10.2f}")

    # -- 3. DUPONT -----------------------------------------------------------
    d3 = dupont.dupont_3step(tfacts, latest)
    d5 = dupont.dupont_5step(tfacts, latest)
    print("\n--- DuPont decomposition of ROE (latest year) ---")
    print(f"   3-step: NetMargin {d3['Net Margin']:.3f} x "
          f"AssetTurn {d3['Asset Turnover']:.3f} x "
          f"EquityMult {d3['Equity Multiplier']:.3f} "
          f"= ROE {d3['ROE (product)']*100:.1f}%")
    print(f"           (direct ROE {d3['ROE (direct)']*100:.1f}%, "
          f"reconciliation diff {d3['Reconciliation diff']:.2e})")
    print(f"   5-step: TaxBurden {d5['Tax Burden']:.3f} x "
          f"IntBurden {d5['Interest Burden']:.3f} x "
          f"OpMargin {d5['Operating Margin']:.3f} x "
          f"AssetTurn {d5['Asset Turnover']:.3f} x "
          f"EquityMult {d5['Equity Multiplier']:.3f} "
          f"= ROE {d5['ROE (product)']*100:.1f}%")

    # -- 4. BENCHMARK --------------------------------------------------------
    bench = benchmark.benchmark_summary(facts_by_ticker, target)
    strong = bench[bench["Standing"] == "Strong"]["Ratio"].tolist()
    weak = bench[bench["Standing"] == "Weak"]["Ratio"].tolist()
    print("\n--- PEER BENCHMARK (latest year, percentile 0-100) ---")
    print(f"   Strong vs peers: {', '.join(strong) if strong else '(none)'}")
    print(f"   Weak vs peers:   {', '.join(weak) if weak else '(none)'}")

    # -- 5. TRENDS -----------------------------------------------------------
    trends = quality.trend_flags(tfacts)
    improving = trends[trends["Trend"] == "Improving"]["Ratio"].tolist()
    deteriorating = trends[trends["Trend"] == "Deteriorating"]["Ratio"].tolist()
    print("\n--- TREND FLAGS (first vs latest year) ---")
    print(f"   Improving:     {', '.join(improving) if improving else '(none)'}")
    print(f"   Deteriorating: {', '.join(deteriorating) if deteriorating else '(none)'}")

    # -- 6. RED FLAGS --------------------------------------------------------
    rf = quality.red_flags(tfacts)
    print("\n--- EARNINGS-QUALITY RED FLAGS (latest year) ---")
    print(f"   Accruals ratio:   {rf.iloc[0][latest]:>7.3f}  -> {rf.iloc[0]['Latest flag']}")
    print(f"   Cash conversion:  {rf.iloc[1][latest]:>7.3f}  -> {rf.iloc[1]['Latest flag']}")

    # -- 7. REPORT -----------------------------------------------------------
    xlsx = reporting.write_excel(facts_by_ticker, target)
    charts = reporting.write_charts(facts_by_ticker, target)
    print("\n--- OUTPUT WRITTEN ---")
    print(f"   Excel: {xlsx}")
    for c in charts:
        print(f"   Chart: {c}")
    print("\nDone. Every number above is a plain ratio you can defend line by line.")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
