"""
forecast.py — the linked three-statement engine (+ debt/revolver cash sweep).
============================================================================
This is the heart of the project. Given the drivers and the opening balance
sheet, it projects the Income Statement (IS), Balance Sheet (BS) and Cash Flow
Statement (CF) forward, all LINKED, so the balance sheet ties out every year.

THE THREE LINKS (say this in an interview):
  1. Net income (IS) flows into retained earnings/equity (BS) and is the top
     line of the cash flow statement (CF).
  2. Depreciation is subtracted on the IS but ADDED BACK on the CF (it's non-cash)
     and it reduces PP&E on the BS.
  3. Ending cash on the CF becomes the cash line on the BS. That is what makes
     the balance sheet balance.

THE DEBT SCHEDULE (the impressive bit):
  - We keep a minimum cash buffer (min_cash_pct of revenue).
  - Any cash ABOVE that buffer is "swept" to pay down debt (revolver first, then
    term debt) — a cash sweep.
  - If cash falls BELOW the buffer, we DRAW on a revolver to top it back up.
  - Interest is charged on the AVERAGE of opening and closing debt. That makes
    the model circular (interest -> net income -> cash -> debt -> interest), so
    we iterate to convergence each year, exactly like Excel's iterative calc.
"""

from __future__ import annotations

import pandas as pd


def build_model(drivers: dict, opening: dict) -> dict:
    """
    Build the linked 5-year model.

    Returns a dict with:
        income, balance, cashflow, debt : DataFrames (rows = lines, cols = years)
        fcff        : DataFrame of the unlevered free-cash-flow build (for the DCF)
        max_imbalance : the largest |assets - (liab+equity)| across all years (~0)
        years       : list of year labels
    """
    a = drivers
    n_years = int(a["forecast_years"])
    yrs = list(range(1, n_years + 1))
    IS, BS, CF, DEBT, FCFF = {}, {}, {}, {}, {}

    # --- carry the opening balances forward as the "prior year" for year 1 ---
    rev_prev = a["start_revenue"]
    ppe_prev = opening["ppe"]
    equity_prev = opening["equity"]
    cash_prev = opening["cash"]
    ar_prev = opening["receivables"]
    inv_prev = opening["inventory"]
    ap_prev = opening["payables"]
    term_prev = opening["term_debt"]
    rev_debt_prev = opening["revolver"]

    for y in yrs:
        # =================================================================
        # INCOME STATEMENT — down to EBIT (does not depend on debt yet)
        # =================================================================
        revenue = rev_prev * (1 + a["revenue_growth"])
        cogs = revenue * (1 - a["gross_margin"])
        gross_profit = revenue - cogs
        opex = revenue * a["opex_pct"]
        depreciation = revenue * a["dep_pct"]
        ebit = gross_profit - opex - depreciation      # operating profit

        # =================================================================
        # WORKING CAPITAL (these balances drive the cash flow)
        # =================================================================
        receivables = revenue * a["dso"] / 365.0       # what customers owe us
        inventory = cogs * a["dio"] / 365.0            # stock we hold
        payables = cogs * a["dpo"] / 365.0             # what we owe suppliers
        change_nwc = ((receivables - ar_prev) + (inventory - inv_prev)
                      - (payables - ap_prev))          # an INCREASE ties up cash

        capex = revenue * a["capex_pct"]
        min_cash = revenue * a["min_cash_pct"]         # the cash buffer to defend
        debt_begin = term_prev + rev_debt_prev

        # =================================================================
        # DEBT SCHEDULE + CASH SWEEP  (solved iteratively for circular interest)
        # -----------------------------------------------------------------
        # interest depends on average debt; average debt depends on the sweep;
        # the sweep depends on cash; cash depends on net income; net income
        # depends on interest. We loop until interest stops moving.
        # =================================================================
        interest = debt_begin * a["interest_rate"]     # first guess: on opening debt
        for _ in range(100):
            ebt = ebit - interest                       # pre-tax profit
            tax = max(ebt, 0.0) * a["tax_rate"]         # no tax benefit if pre-tax < 0
            net_income = ebt - tax
            dividends = max(net_income, 0.0) * a["dividend_payout"]

            # cash before we touch debt = last cash + operating + investing - dividends
            cfo = net_income + depreciation - change_nwc
            cash_before_debt = cash_prev + cfo - capex - dividends

            if cash_before_debt >= min_cash:
                # EXCESS cash -> sweep it against debt (revolver first, then term)
                sweep = cash_before_debt - min_cash
                repay_rev = min(sweep, rev_debt_prev)
                repay_term = min(sweep - repay_rev, term_prev)
                draw = 0.0
                revolver_end = rev_debt_prev - repay_rev
                term_end = term_prev - repay_term
            else:
                # SHORTFALL -> draw the revolver to restore the cash buffer
                draw = min_cash - cash_before_debt
                repay_rev = repay_term = 0.0
                revolver_end = rev_debt_prev + draw
                term_end = term_prev

            debt_end = term_end + revolver_end
            avg_debt = (debt_begin + debt_end) / 2.0
            new_interest = avg_debt * a["interest_rate"]  # interest on AVERAGE debt
            if abs(new_interest - interest) < 1e-9:
                interest = new_interest
                break
            interest = new_interest

        net_debt_change = draw - (repay_rev + repay_term)
        ending_cash = cash_before_debt + net_debt_change

        IS[y] = {
            "Revenue": revenue, "COGS": -cogs, "Gross Profit": gross_profit,
            "Operating Expenses": -opex, "Depreciation": -depreciation,
            "EBIT": ebit, "Interest Expense": -interest, "Pre-Tax Income": ebt,
            "Tax": -tax, "Net Income": net_income,
        }

        CF[y] = {
            "Net Income": net_income, "add: Depreciation": depreciation,
            "less: Change in Working Capital": -change_nwc,
            "Cash from Operations": cfo,
            "Capex": -capex, "Cash from Investing": -capex,
            "Dividends": -dividends,
            "Debt Drawn (Revolver)": draw,
            "Debt Repaid (Sweep)": -(repay_rev + repay_term),
            "Cash from Financing": -dividends + net_debt_change,
            "Net Change in Cash": ending_cash - cash_prev,
            "Ending Cash": ending_cash,
        }

        DEBT[y] = {
            "Debt (opening)": debt_begin,
            "Revolver Drawn": draw,
            "Revolver Repaid": -repay_rev,
            "Term Debt Repaid (Sweep)": -repay_term,
            "Debt (closing)": debt_end,
            "Average Debt": avg_debt,
            "Interest @ rate on avg debt": interest,
        }

        # =================================================================
        # BALANCE SHEET
        # =================================================================
        ppe = ppe_prev + capex - depreciation           # roll PP&E forward
        equity = equity_prev + net_income - dividends    # retained earnings build
        total_assets = ending_cash + receivables + inventory + ppe
        total_liab_equity = payables + debt_end + equity
        balance_check = total_assets - total_liab_equity  # MUST be ~0

        BS[y] = {
            "Cash": ending_cash, "Receivables": receivables, "Inventory": inventory,
            "PP&E (net)": ppe, "Total Assets": total_assets,
            "Payables": payables, "Debt": debt_end, "Equity": equity,
            "Total Liab. + Equity": total_liab_equity,
            "Balance Check (=0)": balance_check,
        }

        # =================================================================
        # UNLEVERED FREE CASH FLOW (FCFF) — feeds the DCF in valuation.py
        # FCFF = EBIT*(1-tax) + D&A - capex - change in NWC
        # (unlevered = before financing, so it ignores interest by design)
        # =================================================================
        nopat = ebit * (1 - a["tax_rate"])              # net operating profit after tax
        fcff = nopat + depreciation - capex - change_nwc
        FCFF[y] = {
            "EBIT": ebit, "NOPAT = EBIT*(1-tax)": nopat,
            "add: Depreciation": depreciation, "less: Capex": -capex,
            "less: Change in NWC": -change_nwc, "FCFF": fcff,
        }

        # --- roll everything forward to next year ---
        rev_prev, ppe_prev, equity_prev = revenue, ppe, equity
        cash_prev, ar_prev, inv_prev, ap_prev = ending_cash, receivables, inventory, payables
        term_prev, rev_debt_prev = term_end, revolver_end

    cols = [f"Year {y}" for y in yrs]
    income = pd.DataFrame(IS).round(1);   income.columns = cols
    balance = pd.DataFrame(BS).round(1);  balance.columns = cols
    cashflow = pd.DataFrame(CF).round(1); cashflow.columns = cols
    debt = pd.DataFrame(DEBT).round(1);   debt.columns = cols
    fcff = pd.DataFrame(FCFF).round(1);   fcff.columns = cols

    max_imbalance = float(balance.loc["Balance Check (=0)"].abs().max())

    return {
        "income": income, "balance": balance, "cashflow": cashflow,
        "debt": debt, "fcff": fcff,
        "max_imbalance": max_imbalance, "years": cols,
    }
