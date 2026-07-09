"""
Options / F&O Analytics — Nifty & Bank Nifty
--------------------------------------------
Computes the core option-chain analytics an F&O desk lives on:
  * PCR (Put-Call Ratio)            — sentiment (>1 bullish/​put-heavy, <1 bearish/​call-heavy)
  * Max Pain                        — the expiry strike that hurts the most option BUYERS
  * OI support / resistance         — highest Put OI = support, highest Call OI = resistance
  * OI build-up classification      — long build-up / short build-up / short covering / long unwinding
    (from the sign of the price change vs the sign of the open-interest change)

DATA: it first tries to pull the LIVE NSE option chain. NSE blocks many automated/cloud requests, so if
that fails it falls back to a clearly-labelled SAMPLE chain so the analytics are still demonstrable. The
output always states which data source was used — the sample is never presented as live.

Run:  python options_analytics.py
"""
import os
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUT, exist_ok=True)

# index -> (NSE option-chain symbol, yfinance ticker, strike step)
INDICES = {
    "NIFTY": {"yf": "^NSEI", "step": 50},
    "BANKNIFTY": {"yf": "^NSEBANK", "step": 100},
}


# ----------------------------- data -----------------------------
def fetch_live_chain(symbol):
    """Try the live NSE option-chain API. Returns (DataFrame, underlying) or None on any failure.
    NSE requires a browser-like session (hit the site first for cookies, then the JSON API)."""
    try:
        import requests
        h = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
             "Accept": "application/json", "Accept-Language": "en-US,en;q=0.9"}
        s = requests.Session()
        s.get("https://www.nseindia.com/option-chain", headers=h, timeout=8)   # collect cookies
        r = s.get(f"https://www.nseindia.com/api/option-chain-indices?symbol={symbol}",
                  headers=h, timeout=8)
        data = r.json()
        spot = float(data["records"]["underlyingValue"])
        rows = []
        for d in data["records"]["data"]:
            ce, pe = d.get("CE", {}), d.get("PE", {})
            rows.append({"strike": d["strikePrice"],
                         "CE_OI": ce.get("openInterest", 0), "CE_chgOI": ce.get("changeinOpenInterest", 0),
                         "CE_IV": ce.get("impliedVolatility", 0),
                         "PE_OI": pe.get("openInterest", 0), "PE_chgOI": pe.get("changeinOpenInterest", 0),
                         "PE_IV": pe.get("impliedVolatility", 0)})
        df = pd.DataFrame(rows).groupby("strike", as_index=False).first().sort_values("strike")
        return df, spot
    except Exception:
        return None


def sample_chain(spot, step):
    """Build a realistic *illustrative* chain around spot — clearly SAMPLE data, used only when the
    live NSE fetch is unavailable. Call OI peaks above spot (resistance), Put OI peaks below (support)."""
    atm = round(spot / step) * step
    strikes = np.arange(atm - 8 * step, atm + 8 * step + step, step)
    rng = np.random.default_rng(7)
    ce_oi, pe_oi = [], []
    for k in strikes:
        d = (k - atm) / step
        # calls: more OI above spot; puts: more OI below spot (bell-ish shapes, offset)
        ce_oi.append(max(2, int(90 * np.exp(-((d - 2) ** 2) / 12) * (1 + 0.15 * rng.standard_normal()))))
        pe_oi.append(max(2, int(90 * np.exp(-((d + 2) ** 2) / 12) * (1 + 0.15 * rng.standard_normal()))))
    return pd.DataFrame({
        "strike": strikes,
        "CE_OI": ce_oi, "CE_chgOI": (rng.integers(-15, 20, len(strikes))).tolist(),
        "CE_IV": np.round(13 + np.abs(strikes - atm) / step * 0.4, 1),
        "PE_OI": pe_oi, "PE_chgOI": (rng.integers(-15, 20, len(strikes))).tolist(),
        "PE_IV": np.round(13 + np.abs(strikes - atm) / step * 0.4, 1),
    }), atm


# ----------------------------- analytics -----------------------------
def pcr(chain):
    """Put-Call Ratio by open interest. > 1 = put-heavy (often read bullish/​support); < 1 = call-heavy."""
    return chain["PE_OI"].sum() / max(chain["CE_OI"].sum(), 1)


def max_pain(chain):
    """Max-pain strike: the expiry price at which the TOTAL intrinsic value owed to option buyers is
    smallest (i.e. the most options expire worthless). Price often gravitates here into expiry."""
    strikes = chain["strike"].values
    pain = []
    for s in strikes:
        call_pay = (np.maximum(s - strikes, 0) * chain["CE_OI"].values).sum()   # ITM calls if expiry = s
        put_pay = (np.maximum(strikes - s, 0) * chain["PE_OI"].values).sum()    # ITM puts if expiry = s
        pain.append(call_pay + put_pay)
    return int(strikes[int(np.argmin(pain))])


def oi_levels(chain):
    """Highest Put OI strike acts as support; highest Call OI strike acts as resistance."""
    support = int(chain.loc[chain["PE_OI"].idxmax(), "strike"])
    resistance = int(chain.loc[chain["CE_OI"].idxmax(), "strike"])
    return support, resistance


def buildup(price_change, oi_change):
    """The classic four-quadrant read of price move vs open-interest move:
       price up + OI up  = Long build-up    (new longs, bullish)
       price down + OI up = Short build-up  (new shorts, bearish)
       price up + OI down = Short covering  (shorts exiting, bullish)
       price down + OI down = Long unwinding (longs exiting, bearish)"""
    up_p, up_oi = price_change >= 0, oi_change >= 0
    if up_p and up_oi:
        return "Long build-up (bullish)"
    if not up_p and up_oi:
        return "Short build-up (bearish)"
    if up_p and not up_oi:
        return "Short covering (bullish)"
    return "Long unwinding (bearish)"


def oi_chart(name, chain, spot, support, resistance):
    fig, ax = plt.subplots(figsize=(10, 4.6))
    w = (chain["strike"].iloc[1] - chain["strike"].iloc[0]) * 0.4
    ax.bar(chain["strike"] - w / 2, chain["CE_OI"], width=w, color="#d73027", alpha=0.8, label="Call OI (resistance)")
    ax.bar(chain["strike"] + w / 2, chain["PE_OI"], width=w, color="#1a9850", alpha=0.8, label="Put OI (support)")
    ax.axvline(spot, color="#1f4e79", lw=2, label=f"Spot {spot:,.0f}")
    ax.axvline(resistance, color="#d73027", ls="--", lw=1.3)
    ax.axvline(support, color="#1a9850", ls="--", lw=1.3)
    ax.set_title(f"{name} — Open Interest by strike")
    ax.set_xlabel("Strike"); ax.set_ylabel("Open Interest"); ax.legend(fontsize=8); ax.grid(alpha=0.25)
    path = os.path.join(OUT, f"options_{name.lower()}_oi.png")
    fig.tight_layout(); fig.savefig(path, dpi=130); plt.close(fig)
    return path


def underlying_change(yf_ticker):
    """Latest close-to-close % change of the index (for the build-up read)."""
    df = yf.download(yf_ticker, period="5d", progress=False, auto_adjust=True)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    c = df["Close"].dropna()
    return float(c.iloc[-1]), float(c.iloc[-1] - c.iloc[-2])


def analyse(name, cfg):
    spot, price_chg = underlying_change(cfg["yf"])
    live = fetch_live_chain(name)
    if live:
        chain, src = live[0], "LIVE (NSE)"
        spot = live[1]
    else:
        chain, atm = sample_chain(spot, cfg["step"])
        src = "SAMPLE (live NSE unavailable)"
    p = pcr(chain)
    mp = max_pain(chain)
    support, resistance = oi_levels(chain)
    oi_chg = int(chain["CE_chgOI"].sum() + chain["PE_chgOI"].sum())
    bu = buildup(price_chg, oi_chg)
    chart = oi_chart(name, chain, spot, support, resistance)
    chain.to_csv(os.path.join(OUT, f"options_{name.lower()}_chain.csv"), index=False)
    return {"name": name, "src": src, "spot": spot, "pcr": p, "max_pain": mp,
            "support": support, "resistance": resistance, "buildup": bu,
            "atm_iv": float(chain.loc[(chain["strike"] - spot).abs().idxmin(), "CE_IV"]), "chart": chart}


def main():
    print("=== Options / F&O Analytics ===")
    for name, cfg in INDICES.items():
        a = analyse(name, cfg)
        print(f"\n{name}   [data: {a['src']}]")
        print(f"  Spot {a['spot']:,.0f}   PCR {a['pcr']:.2f}   Max-pain {a['max_pain']:,}   ATM IV {a['atm_iv']:.1f}%")
        print(f"  OI support {a['support']:,}   OI resistance {a['resistance']:,}")
        print(f"  Build-up: {a['buildup']}")
        print(f"  OI chart -> {a['chart']}")


if __name__ == "__main__":
    main()
