"""
Signal Accuracy Backtest — does the report's signal actually work?
-----------------------------------------------------------------
Re-creates the research engine's confidence-weighted signal at EVERY historical bar (not just the latest)
and measures how often it was right: for each BUY, did price rise over the next N days? for each SELL, did
it fall? This turns "here's a signal" into "this signal has worked X% of the time historically".

Same five weighted categories as the report (Trend 40 / Momentum 25 / Volatility 15 / Mean-Rev 10 /
Structure 10), same overbought/oversold guardrail, evaluated over ~5 years of daily data.

Run:  python signal_accuracy.py
"""
import os
import numpy as np
import pandas as pd
import yfinance as yf

OUT = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUT, exist_ok=True)

ASSETS = {"Nifty 50": "^NSEI", "Bank Nifty": "^NSEBANK", "Gold (COMEX)": "GC=F", "Crude Oil (WTI)": "CL=F"}
WEIGHTS = {"Trend": 0.40, "Momentum": 0.25, "Volatility": 0.15, "Mean-Reversion": 0.10, "Structure": 0.10}
HORIZON = 10        # look 10 trading days (~2 weeks) ahead to judge each signal
SWING = 60          # window for support/resistance, matching the daily report


def signals(df):
    """Compute the BUY/SELL/HOLD signal at every bar (vectorised) exactly as the report would."""
    c = df["Close"]
    sma20, sma50 = c.rolling(20).mean(), c.rolling(50).mean()
    std20 = c.rolling(20).std()
    d = c.diff()
    rsi = 100 - 100 / (1 + d.clip(lower=0).rolling(14).mean() /
                       (-d.clip(upper=0)).rolling(14).mean().replace(0, np.nan))
    macd = c.ewm(span=12, adjust=False).mean() - c.ewm(span=26, adjust=False).mean()
    sig = macd.ewm(span=9, adjust=False).mean()
    support, resistance = c.rolling(SWING).min(), c.rolling(SWING).max()
    rng = (resistance - support).replace(0, np.nan)

    clip = lambda x: np.clip(x, -1, 1)
    trend = clip((np.where(c > sma20, 1, -1) + np.where(sma20 > sma50, 1, -1)) / 2)
    momentum = clip((np.where(macd > sig, 1, -1) + clip((rsi - 50) / 20)) / 2)
    volatility = clip((c - sma20) / (2 * std20))
    meanrev = clip((50 - rsi) / 30)
    structure = clip(1 - 2 * (c - support) / rng)

    net = (WEIGHTS["Trend"] * trend + WEIGHTS["Momentum"] * momentum +
           WEIGHTS["Volatility"] * volatility + WEIGHTS["Mean-Reversion"] * meanrev +
           WEIGHTS["Structure"] * structure)
    view = pd.Series(np.where(net >= 0.20, "BUY", np.where(net <= -0.20, "SELL", "HOLD")), index=c.index)
    # same guardrail as the report
    view[(view == "SELL") & (rsi < 25)] = "HOLD"
    view[(view == "BUY") & (rsi > 80)] = "HOLD"
    return view


def accuracy(name, ticker):
    df = yf.download(ticker, period="5y", progress=False, auto_adjust=True)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df = df[["Open", "High", "Low", "Close"]].dropna()
    view = signals(df)
    fwd = df["Close"].shift(-HORIZON) / df["Close"] - 1     # forward N-day return
    ok = view.notna() & fwd.notna()

    buys = ok & (view == "BUY")
    sells = ok & (view == "SELL")
    buy_win = (fwd[buys] > 0).mean() * 100 if buys.any() else np.nan      # BUY right if price rose
    sell_win = (fwd[sells] < 0).mean() * 100 if sells.any() else np.nan   # SELL right if price fell
    # overall directional accuracy across all actionable signals
    correct = ((view == "BUY") & (fwd > 0)) | ((view == "SELL") & (fwd < 0))
    acts = buys | sells
    overall = correct[acts].mean() * 100 if acts.any() else np.nan
    return {"Asset": name, "BUY signals": int(buys.sum()), "BUY win %": buy_win,
            "SELL signals": int(sells.sum()), "SELL win %": sell_win,
            "Overall accuracy %": overall}


def main():
    print(f"=== Signal Accuracy Backtest (forward horizon = {HORIZON} trading days, ~5y daily) ===\n")
    rows = [accuracy(n, t) for n, t in ASSETS.items()]
    out = pd.DataFrame(rows)
    fmt = out.copy()
    for col in ["BUY win %", "SELL win %", "Overall accuracy %"]:
        fmt[col] = fmt[col].map(lambda v: "-" if pd.isna(v) else f"{v:.0f}%")
    print(fmt.to_string(index=False))
    out.to_csv(os.path.join(OUT, "signal_accuracy.csv"), index=False)
    print(f"\nCSV -> {os.path.join(OUT, 'signal_accuracy.csv')}")
    print("Note: directional accuracy over the next ~2 weeks; not a tradable P&L (no costs/stops/sizing).")


if __name__ == "__main__":
    main()
