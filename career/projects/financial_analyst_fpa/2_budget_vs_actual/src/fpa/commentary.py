"""
commentary.py - turn the numbers into plain-English sentences.

Every FP&A pack ends with written commentary: the CFO does not want to read a
grid of numbers, they want "Beta revenue was $X unfavorable, driven by a volume
shortfall of N units, partly offset by favorable pricing." This module builds
those sentences straight from the variance tables so the words can never drift
out of sync with the figures.
"""

from .variance import product_variance, pvm_decomposition, opex_variance


def money(x):
    """Format a signed dollar figure like +$12,340 or -$3,400."""
    return f"{'+' if x >= 0 else '-'}${abs(int(round(x))):,}"


def pct(x):
    return f"{x:+.1f}%"


def _pvm_per_product(budget, actuals):
    """Return the PVM table without the TOTAL row, indexed by product."""
    pvm = pvm_decomposition(budget, actuals)
    return pvm.drop(index="TOTAL")


def revenue_commentary(budget, actuals):
    """One sentence per product explaining its revenue variance via P/V/M."""
    pvm = _pvm_per_product(budget, actuals)
    lines = []
    for product in pvm.index:
        total = pvm.loc[product, "Total Var"]
        price = pvm.loc[product, "Price"]
        vol = pvm.loc[product, "Volume"]
        mix = pvm.loc[product, "Mix"]
        direction = "favorable" if total > 0 else "unfavorable"

        # Identify the biggest driver by absolute size for the headline phrase.
        pieces = {"price": price, "volume": vol, "mix": mix}
        words = {"price": "pricing", "volume": "volume", "mix": "product mix"}
        driver = max(pieces, key=lambda k: abs(pieces[k]))
        driver_word = words[driver]

        # Note the largest OFFSET (an effect pushing the other way), if any.
        offsets = {k: v for k, v in pieces.items()
                   if (v > 0) != (total > 0) and abs(v) > 1}
        offset_txt = ""
        if offsets:
            off = max(offsets, key=lambda k: abs(offsets[k]))
            offset_txt = f", partly offset by {money(offsets[off])} of {words[off]}"

        lines.append(
            f"{product} revenue was {money(total)} {direction}, driven mainly by "
            f"{driver_word} ({money(pieces[driver])}){offset_txt}. "
            f"[price {money(price)}, volume {money(vol)}, mix {money(mix)}]"
        )
    return lines


def cost_commentary(budget, actuals):
    """Sentences on the biggest COGS and opex stories."""
    pv = product_variance(budget, actuals)
    ov = opex_variance(budget, actuals)
    lines = []

    # Worst gross-margin product (COGS running hot relative to plan).
    worst_cogs = pv["COGS Var"].idxmax()
    if pv.loc[worst_cogs, "COGS Var"] > 0:
        lines.append(
            f"{worst_cogs} COGS ran {money(pv.loc[worst_cogs, 'COGS Var'])} over "
            f"budget (unfavorable) - a unit-cost/efficiency issue to investigate."
        )

    # Biggest opex overspend.
    worst_opex = ov["Opex Var"].idxmax()
    if ov.loc[worst_opex, "Opex Var"] > 0:
        lines.append(
            f"{worst_opex} overspent by {money(ov.loc[worst_opex, 'Opex Var'])} "
            f"(unfavorable) versus its cost-centre budget."
        )

    # Biggest opex saving.
    best_opex = ov["Opex Var"].idxmin()
    if ov.loc[best_opex, "Opex Var"] < 0:
        lines.append(
            f"On the upside, {best_opex} came in {money(ov.loc[best_opex, 'Opex Var'])} "
            f"under budget (favorable saving)."
        )
    return lines


def kpi_commentary(kpis):
    """Two-sentence executive summary built from the KPI dict."""
    fav_name, fav_val = kpis["largest_favorable"]
    unf_name, unf_val = kpis["largest_unfavorable"]
    return [
        f"Full-year revenue landed at {money(kpis['actual_revenue'])} versus a "
        f"{money(kpis['budget_revenue'])} plan ({pct(kpis['revenue_var_pct'])}); "
        f"operating profit finished {money(kpis['operating_profit_var'])} versus plan.",
        f"Gross margin moved from {kpis['budget_gross_margin_pct']:.1f}% (plan) to "
        f"{kpis['actual_gross_margin_pct']:.1f}% (actual). Largest favorable driver: "
        f"{fav_name} ({money(fav_val)}); largest unfavorable: {unf_name} ({money(unf_val)}).",
    ]
