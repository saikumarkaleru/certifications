# Chapter 64: Reading the Options Market in Code — PCR, Max-Pain, OI & India VIX

## Intro / the big idea

Every weekday, lakhs of option contracts trade on Nifty and Bank Nifty, and the exchange publishes a snapshot of where all that money is sitting: the **option chain**. Buried in those columns of open interest and price are crude but useful clues about what the crowd is betting on — where it thinks the index is "pinned", which strikes it treats as a floor and a ceiling, and how nervous it is about the next move. Professional desks read this every morning. The good news is that you do not need a Bloomberg terminal to do the same; the National Stock Exchange (NSE) gives the raw data away for free, and about forty lines of Python turn it into a dashboard.

This chapter is a hands-on build. We are going to fetch the live NSE option chain, parse it, and compute four classic "derivatives sentiment" reads — the **Put-Call Ratio (PCR)**, **Max Pain**, **OI-based support and resistance**, and an **India VIX expected move**. Then we will fold them into one simple "derivatives bias" summary. This mirrors a real options-market-reader module you would put inside a trading project. Throughout, keep one honest fact in mind: these are *sentiment hints*, not a crystal ball. They tell you where the crowd is leaning. The crowd is often wrong at exactly the wrong moment.

## Core concepts

### What is in the option chain

The option chain is a table. Each row is a **strike price** (e.g., 24000, 24100, 24200). For each strike, the left half shows the **Call (CE)** side and the right half shows the **Put (PE)** side. The columns we care about are:

- **Open Interest (OI)** — the number of contracts currently *open* (not yet closed or expired) at that strike. Think of OI as the size of the bet parked at a strike. High call OI means many people have written or bought calls there; high put OI means the same for puts.
- **Change in OI** — how much OI grew or shrank since the previous day. Fresh OI build-up shows where new positions are forming today.
- **Last Traded Price (LTP)** — the premium the option last traded at.
- **Implied Volatility (IV)** — the market's volatility expectation baked into that option's price.

Open interest is the key ingredient. Volume tells you how much changed hands; **OI tells you how much is still on the table.** Standing bets matter more than completed trades for reading sentiment.

### The NSE option-chain endpoint (and why it is fiddly)

NSE publishes the chain through a public JSON endpoint used by its own website:

```
https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY
```

You cannot just `requests.get()` it cold. NSE's servers reject requests that do not look like a real browser. In practice you must:

1. Send realistic **headers** — a `User-Agent`, `Accept`, and `Accept-Language` — so the request looks like Chrome.
2. First hit the **home page** (`https://www.nseindia.com`) to pick up session **cookies**, then reuse the same `requests.Session` for the API call.
3. Run it from a **normal residential/office machine**. Cloud IPs (AWS, etc.) are frequently blocked, and the endpoint rate-limits aggressively. Add a small delay and a retry.

Because of this, robust code always carries a **fallback to sample data** so the rest of your analysis can be developed and tested offline. We do exactly that below.

### Put-Call Ratio (PCR) — a contrarian mood ring

The PCR is the simplest sentiment gauge:

```
PCR (OI) = total Put OI / total Call OI
```

Intuition: puts are bought as downside insurance (bearish/defensive); calls are bought for upside (bullish). So you might *think* a high PCR means everyone is bearish. The professional reading is the opposite — it is treated as a **contrarian** indicator:

- **PCR > ~1.3–1.5**: unusually heavy put activity. The crowd is heavily hedged/bearish — often a sign of *excess fear*, which can mark a bottom. Mildly bullish contrarian signal.
- **PCR < ~0.7**: unusually heavy call activity. The crowd is complacent/greedy — *excess optimism*, which can precede a pullback. Mildly bearish contrarian signal.
- **PCR ~0.9–1.1**: neutral / balanced.

These thresholds are rules of thumb for Indian index options, not laws. PCR is most useful at *extremes* and when *changing* — a PCR rising from 0.8 to 1.4 over a week says more than its absolute level.

### Max Pain — where the most options expire worthless

Here is a striking idea. Option *buyers* mostly lose; option *sellers* (writers) mostly collect premium. Sellers tend to be better-capitalised institutions. There is a long-observed tendency for the index to drift, near expiry, toward the strike where the **total payout to all option holders is minimised** — i.e., where the largest rupee value of options expires worthless. That strike is called **Max Pain** (maximum pain for buyers).

The algorithm is mechanical. For each *candidate* settlement strike `S`, compute what writers would have to pay out across every strike:

```
For a candidate expiry price S:
  Call payout at strike K = max(S - K, 0) * (Call OI at K)   # ITM calls cost writers
  Put  payout at strike K = max(K - S, 0) * (Put  OI at K)   # ITM puts  cost writers
  Total pain(S) = sum over all K of (Call payout + Put payout)

Max Pain strike = the S that MINIMISES Total pain(S)
```

You evaluate this at every listed strike and pick the minimum. Near expiry, Max Pain often acts like a magnet — a "pin". Far from expiry it is much weaker and shifts as OI rebuilds. It is a tendency, not a guarantee; a strong trend or a news shock overrides it easily.

### OI-based support and resistance

This one is beautifully intuitive:

- **Resistance = the strike with the highest Call OI.** Call writers (often institutions) have sold calls there and want the index to stay *below* that strike so those calls expire worthless. Their hedging activity tends to cap the index near it.
- **Support = the strike with the highest Put OI.** Put writers want the index to stay *above* that strike, so heavy put OI tends to act as a floor.

So if 24000 has the fattest put OI and 24500 the fattest call OI, the crowd's implied trading range for the expiry is roughly 24000–24500. These levels are watched by everyone, which is partly *why* they hold — they are self-fulfilling until a strong move breaks them.

### India VIX → expected move

**India VIX** is the index of expected 30-day volatility derived from Nifty option prices (NSE's version of the CBOE VIX method). It is quoted as an **annualised percentage**. A VIX of 14 means the market expects Nifty to move within a +/-14% band over the next year, with about 68% probability (one standard deviation).

To get an expected move over a *shorter* horizon, scale by the square root of time:

```
Expected move (1 sigma, fraction) = (VIX / 100) * sqrt(days / 365)
Expected move in points = Spot * Expected move fraction
```

So at Nifty 24000 with VIX 14, the expected one-week (7-day) move is roughly:

```
0.14 * sqrt(7/365) = 0.14 * 0.1385 = 0.0194  -> about 1.94%
24000 * 0.0194 ≈ 465 points (1 sigma)
```

Meaning: with ~68% confidence, Nifty stays within about +/-465 points over the week. Multiply by 2 for the ~95% (2-sigma) band. This is the single most useful number for sizing expectations, picking strikes, and judging whether a straddle is cheap or dear.

### Combining into a "derivatives bias"

No single number decides anything. The pro move is to combine the reads into a quick scorecard:

1. **PCR** → contrarian lean (very high = bullish-ish, very low = bearish-ish).
2. **Spot vs Max Pain** → if spot is well above Max Pain near expiry, there is a downward "pin" pull, and vice versa.
3. **OI support/resistance** → the expected range; note where spot sits inside it.
4. **VIX** → how wide the expected move is (conviction sizing).

Each gives a small +1 / 0 / -1 vote; sum them for a coarse bias. Treat the output as a *hypothesis to confirm with price action*, never a trade trigger on its own.

## Worked example (₹, Nifty)

Suppose we fetch the weekly Nifty chain and (after filtering to one expiry) get this small slice. Spot Nifty = **24,180**, India VIX = **13.5**, days to expiry = **4**.

| Strike | Call OI | Put OI |
|-------:|--------:|-------:|
| 23800  | 12,00,000 | 9,00,000  |
| 23900  | 10,00,000 | 14,00,000 |
| 24000  | 18,00,000 | 30,00,000 |
| 24100  | 22,00,000 | 20,00,000 |
| 24200  | 35,00,000 | 12,00,000 |
| 24300  | 40,00,000 | 6,00,000  |
| 24400  | 28,00,000 | 4,00,000  |

**PCR:** total Put OI = 95,00,000; total Call OI = 1,65,00,000. PCR = 95/165 = **0.58**. That is low — heavy call writing, a complacent/greedy crowd, a mild *contrarian-bearish* tilt.

**Support / Resistance:** highest Put OI is at **24000** (30,00,000) → support. Highest Call OI is at **24300** (40,00,000) → resistance. Implied range for the week: **24000–24300**, with spot 24180 sitting in the upper-middle.

**Max Pain (sketch for candidate S = 24100):**
- Call payouts: only strikes below 24100 are ITM for calls. 23800: (24100-23800)*12,00,000 = 36,00,00,000... etc. Put payouts: only strikes above 24100. You repeat for every candidate strike. Doing the full sum (the code below does it for us) gives the minimum total pain at **24100**. So Max Pain = 24100, just below spot (24180) — a slight downward pin pull toward expiry.

**VIX expected move:** 0.135 * sqrt(4/365) = 0.135 * 0.1047 = 0.01413 → 1.41%. In points: 24180 * 0.01413 ≈ **342 points (1 sigma)**. So ~68% odds Nifty stays in 23838–24522 this week; ~95% in 23496–24864.

**Combined read:** PCR low (mild bearish), spot above Max Pain (mild bearish pull), spot near the call-OI resistance at 24300 (limited upside room), expected move modest (~340 pts). The derivatives bias is **mildly bearish-to-rangebound**, with 24300 as the wall to watch and 24000 as the floor. A trader might lean toward range/credit strategies rather than buying calls here — *after* confirming with price action.

## The code — a runnable options-market reader

The functions below take a **parsed chain** (a list of dicts) and compute everything. The fetcher tries NSE and **falls back to a built-in sample** so the file runs anywhere.

```python
"""
options_reader.py — read NSE index option chain: PCR, Max Pain, OI levels, VIX move.
Pure-stdlib analytics; fetch uses `requests` if available, else falls back to sample.
"""
from math import sqrt


# ----------------------------------------------------------------------
# 1. FETCH + PARSE  (best-effort; falls back to sample data offline)
# ----------------------------------------------------------------------
def fetch_option_chain(symbol="NIFTY"):
    """
    Try the public NSE option-chain endpoint. Needs browser-like headers and a
    warm-up request to collect cookies. Best run from a normal (non-cloud) machine.
    Returns NSE's raw JSON dict, or None on any failure.
    """
    try:
        import requests
    except ImportError:
        return None

    base = "https://www.nseindia.com"
    url = f"{base}/api/option-chain-indices?symbol={symbol}"
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/124.0 Safari/537.36"),
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
    }
    try:
        sess = requests.Session()
        sess.headers.update(headers)
        sess.get(base, timeout=5)               # warm-up: collect cookies
        resp = sess.get(url, timeout=5)         # actual API call, same session
        if resp.status_code == 200:
            return resp.json()
    except Exception:
        pass
    return None


def parse_chain(raw, expiry=None):
    """
    Flatten NSE's nested JSON into rows: {strike, call_oi, put_oi, call_ltp, put_ltp}.
    If `expiry` (a date string like '04-Jul-2024') is given, keep only that expiry.
    Returns (spot, rows).
    """
    records = raw["records"]
    spot = records["underlyingValue"]
    rows = []
    for item in records["data"]:
        if expiry and item.get("expiryDate") != expiry:
            continue
        ce, pe = item.get("CE"), item.get("PE")
        rows.append({
            "strike":   item["strikePrice"],
            "call_oi":  ce["openInterest"] if ce else 0,
            "put_oi":   pe["openInterest"] if pe else 0,
            "call_ltp": ce["lastPrice"]    if ce else 0.0,
            "put_ltp":  pe["lastPrice"]    if pe else 0.0,
        })
    rows.sort(key=lambda r: r["strike"])
    return spot, rows


# ----------------------------------------------------------------------
# 2. ANALYTICS  (work on a parsed `rows` list — no network needed)
# ----------------------------------------------------------------------
def put_call_ratio(rows):
    """PCR by open interest = total put OI / total call OI."""
    total_put  = sum(r["put_oi"]  for r in rows)
    total_call = sum(r["call_oi"] for r in rows)
    return total_put / total_call if total_call else float("inf")


def max_pain(rows):
    """
    Strike that minimises total payout to option holders (most options expire
    worthless). Evaluate total 'pain' at every listed strike as a candidate
    expiry price; return the minimising strike.
    """
    strikes = [r["strike"] for r in rows]
    best_strike, best_pain = None, None
    for s in strikes:                      # candidate settlement price
        pain = 0.0
        for r in rows:
            k = r["strike"]
            pain += max(s - k, 0) * r["call_oi"]   # ITM calls cost call writers
            pain += max(k - s, 0) * r["put_oi"]    # ITM puts  cost put  writers
        if best_pain is None or pain < best_pain:
            best_pain, best_strike = pain, s
    return best_strike


def oi_support_resistance(rows):
    """Support = strike with max put OI; Resistance = strike with max call OI."""
    support    = max(rows, key=lambda r: r["put_oi"])["strike"]
    resistance = max(rows, key=lambda r: r["call_oi"])["strike"]
    return support, resistance


def expected_move(spot, vix, days):
    """
    1-sigma expected move from India VIX (annualised %), scaled to `days`.
    Returns (fraction, points). Multiply points by 2 for ~95% band.
    """
    frac = (vix / 100.0) * sqrt(days / 365.0)
    return frac, spot * frac


def derivatives_bias(spot, rows, vix, days):
    """Combine the reads into a coarse -2..+2 bias score (+ = bullish)."""
    pcr = put_call_ratio(rows)
    mp  = max_pain(rows)
    support, resistance = oi_support_resistance(rows)
    frac, pts = expected_move(spot, vix, days)

    score = 0
    # PCR as a CONTRARIAN gauge
    if pcr > 1.3:   score += 1          # excess fear -> contrarian bullish
    elif pcr < 0.7: score -= 1          # excess greed -> contrarian bearish
    # Spot vs Max Pain pin
    if spot > mp * 1.002:   score -= 1  # pin pulls down
    elif spot < mp * 0.998: score += 1  # pin pulls up

    label = {2: "Bullish", 1: "Mildly bullish", 0: "Neutral / rangebound",
             -1: "Mildly bearish", -2: "Bearish"}.get(score, "Neutral")
    return {
        "pcr": round(pcr, 2), "max_pain": mp,
        "support": support, "resistance": resistance,
        "expected_move_pts": round(pts, 0),
        "range_1sigma": (round(spot - pts), round(spot + pts)),
        "score": score, "bias": label,
    }


# ----------------------------------------------------------------------
# 3. SAMPLE DATA  (so this runs with no internet)
# ----------------------------------------------------------------------
SAMPLE_SPOT, SAMPLE_VIX, SAMPLE_DAYS = 24180, 13.5, 4
SAMPLE_ROWS = [
    {"strike": 23800, "call_oi": 1200000, "put_oi":  900000, "call_ltp": 0, "put_ltp": 0},
    {"strike": 23900, "call_oi": 1000000, "put_oi": 1400000, "call_ltp": 0, "put_ltp": 0},
    {"strike": 24000, "call_oi": 1800000, "put_oi": 3000000, "call_ltp": 0, "put_ltp": 0},
    {"strike": 24100, "call_oi": 2200000, "put_oi": 2000000, "call_ltp": 0, "put_ltp": 0},
    {"strike": 24200, "call_oi": 3500000, "put_oi": 1200000, "call_ltp": 0, "put_ltp": 0},
    {"strike": 24300, "call_oi": 4000000, "put_oi":  600000, "call_ltp": 0, "put_ltp": 0},
    {"strike": 24400, "call_oi": 2800000, "put_oi":  400000, "call_ltp": 0, "put_ltp": 0},
]


def load_data():
    """Use live NSE data if reachable, otherwise the offline sample."""
    raw = fetch_option_chain("NIFTY")
    if raw:
        # In real use, pick the nearest weekly expiry from raw['records']['expiryDates']
        spot, rows = parse_chain(raw)
        return spot, rows, None, None     # plug in live VIX/days separately
    print("(Using offline sample data — NSE fetch unavailable.)")
    return SAMPLE_SPOT, SAMPLE_ROWS, SAMPLE_VIX, SAMPLE_DAYS


if __name__ == "__main__":
    spot, rows, vix, days = load_data()
    vix  = vix  if vix  is not None else 13.5   # supply live India VIX
    days = days if days is not None else 4       # days to expiry

    print(f"Spot: {spot}   India VIX: {vix}   Days to expiry: {days}")
    report = derivatives_bias(spot, rows, vix, days)
    for k, v in report.items():
        print(f"  {k:18}: {v}")
```

Running it offline prints:

```
(Using offline sample data — NSE fetch unavailable.)
Spot: 24180   India VIX: 13.5   Days to expiry: 4
  pcr               : 0.58
  max_pain          : 24100
  support           : 24000
  resistance        : 24300
  expected_move_pts : 342.0
  range_1sigma      : (23838, 24522)
  score             : -2
  bias              : Bearish
```

That matches the hand calculation: PCR 0.58 (low/contrarian-bearish), Max Pain 24100 below spot (downward pin), support 24000, resistance 24300, ~342-point weekly sigma. The combined score lands bearish-to-rangebound — a *hypothesis*, to confirm with price.

## Common mistakes / risk note

- **Treating these as signals, not hints.** PCR, Max Pain and OI levels are *sentiment context*. They are right often enough to be worth watching and wrong often enough to wreck an account if traded blindly. Around 9 in 10 retail F&O traders lose money (SEBI studies); "the chain said so" is not edge.
- **Reading PCR the wrong way.** Newcomers think high PCR = bearish. Professionally it is read as a *contrarian* extreme gauge. And the absolute number is less informative than its *change* and how it compares to that index's own recent range.
- **Over-trusting Max Pain early in the cycle.** The pin effect is meaningful mainly in the **last day or two** before expiry, and only absent strong trends or news. On Monday of expiry week it is weak; do not anchor to it.
- **Mixing expiries.** NSE's raw JSON contains *all* listed expiries. If you sum OI across every expiry your PCR and Max Pain are meaningless. Always **filter to a single expiry** first (the `expiry` argument above).
- **Forgetting it is a snapshot.** OI updates through the day; a morning read can flip by afternoon. Re-fetch before acting.
- **Fetching from the cloud.** The NSE endpoint blocks many datacenter IPs and rate-limits. Expect failures; that is why the fallback exists. Do not hammer it — add delays, cache, and respect the site.
- **Static thresholds.** 1.3 / 0.7 PCR cutoffs and the VIX bands are rules of thumb. Calibrate to the instrument and regime.

## Key takeaways

- The **NSE option-chain endpoint** is free but needs browser headers, a warm-up request for cookies, and ideally a non-cloud IP; always code a **sample fallback**.
- **PCR = total put OI / total call OI**, read as a **contrarian** gauge — extremes (>~1.3 fearful, <~0.7 greedy) matter more than the middle.
- **Max Pain** is the strike minimising total holder payout; it acts as a weak magnet **near expiry**, not early.
- **OI support = heaviest put-OI strike; resistance = heaviest call-OI strike** — together they sketch the crowd's expected range.
- **India VIX → expected move** via `Spot * (VIX/100) * sqrt(days/365)` gives the ~68% one-sigma band; double it for ~95%.
- Combine the reads into a coarse **bias score**, but treat it as a hypothesis to confirm with price action — never a standalone trigger.

## Practice problems

1. **PCR computation.** A Nifty expiry shows total Call OI = 1,80,00,000 and total Put OI = 2,52,00,000. Compute the PCR and give the contrarian interpretation.

2. **Max Pain, by hand.** Three strikes carry this OI — 24000: Call 10,00,000 / Put 30,00,000; 24100: Call 20,00,000 / Put 20,00,000; 24200: Call 30,00,000 / Put 10,00,000. Treating only these three as candidate settlement prices, which strike is Max Pain?

3. **Expected move.** Bank Nifty spot is 52,000 and India VIX is 16. Compute the 1-sigma expected move (points) over the next 5 days, and the approximate 95% range.

4. **Support / resistance read.** On a chain, the fattest put OI is at 24500 and the fattest call OI at 25000, with spot at 24800. State the implied range and where spot sits in it. What does breaking 25000 on heavy call *unwinding* suggest?

5. **Combine it.** Spot 24180, PCR 1.45, Max Pain 24300, VIX 12, 3 days to expiry. Using the chapter's voting logic, compute the bias score and the 1-sigma range.

6. **Code reasoning.** Why must `parse_chain` filter to a single `expiryDate` before `max_pain` is called? What goes wrong if you don't?

## Solutions

**1.** PCR = 2,52,00,000 / 1,80,00,000 = **1.40**. That is above ~1.3 — heavy put activity, an over-hedged/fearful crowd. As a *contrarian* read it leans **mildly bullish** (fear extremes can mark bottoms). Confirm with price; a single reading is weak.

**2.** Evaluate total pain at each candidate:
- **S = 24000:** Calls ITM: none below 24000 here → 0. Puts ITM (K>S): 24100 put (100*20,00,000=20,00,00,000) + 24200 put (200*10,00,000=20,00,00,000) = 40,00,00,000. Total ≈ **40 cr-units**.
- **S = 24100:** Calls ITM (K<S): 24000 call (100*10,00,000=10,00,00,000). Puts ITM (K>S): 24200 put (100*10,00,000=10,00,00,000). Total = **20 cr-units**.
- **S = 24200:** Calls ITM: 24000 call (200*10,00,000=20,00,00,000) + 24100 call (100*20,00,000=20,00,00,000)=40,00,00,000. Puts ITM: none above. Total ≈ **40 cr-units**.

Minimum is at **24100** → Max Pain = 24100. (Note it sits where call and put OI are balanced — typical.)

**3.** frac = (16/100) * sqrt(5/365) = 0.16 * sqrt(0.013699) = 0.16 * 0.11704 = 0.018726. Points = 52,000 * 0.018726 ≈ **974 points (1 sigma)**. The ~95% (2-sigma) range ≈ 52,000 +/- 1,948 → roughly **50,052 to 53,948**.

**4.** Implied range is **24500 (support) to 25000 (resistance)**; spot 24800 sits in the **upper third**, nearer resistance, so less room above than below. If 25000 breaks while that call OI is being **unwound** (call writers buying back/covering), it signals writers capitulating — bullish: the ceiling is being removed, often fuelling a further up-move.

**5.** PCR 1.45 > 1.3 → contrarian **+1**. Spot 24180 vs Max Pain 24300: spot is *below* Max Pain (24180 < 24300*0.998 = 24251) → upward pin → **+1**. Score = **+2 → "Bullish"**. Expected move: frac = 0.12 * sqrt(3/365) = 0.12 * 0.09068 = 0.010882; points = 24180 * 0.010882 ≈ **263**. 1-sigma range ≈ **23,917 to 24,443**.

**6.** NSE's `records.data` lists *every* listed expiry (current week, next week, monthly...). If you don't filter, `max_pain` sums OI from unrelated expiries that settle on different dates — the payout math becomes meaningless because those contracts will not all settle at the same price on the same day. PCR is similarly distorted (near-month OI dwarfs far months, or vice versa). Filtering to one `expiryDate` ensures every contract in the calculation shares one settlement event, which is the entire premise of Max Pain and a clean PCR.
