"""
Generate the closing reference chapter of the encyclopedia:
encyclopedia/E13_matrix.md  — a computed 200-strategy quick-reference matrix + decision tables.
All numbers come straight from strategies_metrics.json (nothing hand-typed).
Run:  python make_reference_matrix.py
"""
import os, json

ROOT = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(ROOT, "strategies_metrics.json"), encoding="utf-8"))
OUT = os.path.join(ROOT, "encyclopedia", "E13_matrix.md")

CAT_ORDER = [
    "Single-Leg & Stock Combinations", "Vertical Spreads",
    "Straddles, Strangles & Volatility", "Butterflies", "Condors",
    "Ratio Spreads & Backspreads", "Calendars & Diagonals",
    "Covered & Income Strategies", "Hedging & Protective Strategies",
    "Synthetics & Arbitrage", "Exotic & Named Combinations",
    "Deployments, Ladders & When-to-Use Playbooks",
]


def mp(r):
    return "Unlimited" if r["max_profit_unlimited"] else f"{r['max_profit']:+.0f}"

def ml(r):
    return "Undefined" if r["max_loss_unlimited"] else f"{r['max_loss']:+.0f}"

def rr(r):
    return "—" if r["risk_reward"] is None else f"{r['risk_reward']:.2f}"

def be(r):
    return ", ".join(f"{b:.0f}" for b in r["breakevens"]) or "—"

def net(r):
    v = r["net_cost"]
    if abs(v) > 3000:            # stock-based: the ~24000 index outlay dominates
        return ("debit" if v > 0 else "credit") + " (incl. index)"
    return f"{'debit' if v > 0 else 'credit'} {abs(v):.0f}"


L = []
w = L.append

w("# Strategy Group 13: The 200-Strategy Quick-Reference Matrix\n")
w("This closing chapter is your index into the whole encyclopedia. Every figure below is computed by the "
  "same Black-Scholes engine used throughout, on Nifty at 24,000 (points per unit; multiply by the lot of "
  "about 75 for rupees). Use the master tables to scan a whole family at a glance, then the decision "
  "tables to jump straight to the structures that fit your view, your volatility read and your risk "
  "appetite. \"Max profit/loss\" are in points at the modelled strikes; \"R:R\" is reward-to-risk for "
  "defined-risk trades (a dash means one side is unlimited or undefined).\n")

# ---------------- master tables by category ----------------
w("## Master matrix — all 200 strategies by family\n")
for i, cat in enumerate(CAT_ORDER, 1):
    rows = [r for r in D if r["category"] == cat]
    w(f"\n### Group {i}: {cat} ({len(rows)})\n")
    w("| # | Strategy | View | Vol | Net | Max P (pts) | Max L (pts) | R:R | Breakeven(s) |")
    w("|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        w(f"| {r['n']} | {r['name']} | {r['view']} | {r['vol']} | {net(r)} | "
          f"{mp(r)} | {ml(r)} | {rr(r)} | {be(r)} |")
    w("")

# ---------------- decision tables ----------------
w("\n## Decision table A — by directional view\n")
buckets = {
    "Bullish": lambda v: "bull" in v.lower() or "bullish" in v.lower(),
    "Bearish": lambda v: "bear" in v.lower(),
    "Neutral / range-bound": lambda v: "range" in v.lower() or "neutral" in v.lower() or "pin" in v.lower(),
    "Expecting a big move / breakout": lambda v: "move" in v.lower() or "breakout" in v.lower() or "big" in v.lower(),
}
for label, fn in buckets.items():
    names = [f"{r['name']} (#{r['n']})" for r in D if fn(r["view"])]
    w(f"\n**{label}** — {len(names)} structures:\n")
    w("> " + "; ".join(names) + ".\n")

w("\n## Decision table B — by volatility posture\n")
volmap = {
    "Long volatility / vega (buy when IV is LOW)": lambda v: "long" in v.lower(),
    "Short volatility / vega (sell when IV is HIGH)": lambda v: "short" in v.lower(),
    "Vega-light / direction- or skew-driven": lambda v: "neutral" in v.lower() or "low" in v.lower() or "skew" in v.lower() or "mixed" in v.lower() or "none" in v.lower(),
}
for label, fn in volmap.items():
    names = [f"{r['name']} (#{r['n']})" for r in D if fn(r["vol"])]
    w(f"\n**{label}** — {len(names)} structures:\n")
    w("> " + "; ".join(names) + ".\n")

w("\n## Decision table C — defined risk vs undefined (uncapped) risk\n")
undefined = [r for r in D if r["max_loss_unlimited"]]
zerofloor = [r for r in D if (not r["max_loss_unlimited"]) and r["max_loss"] is not None and r["max_loss"] < -5000]
w("\n**Truly uncapped loss — size tiny, always define or hedge the tail:**\n")
w("> " + "; ".join(f"{r['name']} (#{r['n']})" for r in undefined) + ".\n")
w("\n**\"Bounded but catastrophic\" — the worst case assumes the index falls to zero (naked-put / "
  "stock-owning trades). Manage long before that:**\n")
w("> " + "; ".join(f"{r['name']} (#{r['n']})" for r in zerofloor) + ".\n")

w("\n## Decision table D — highest reward-to-risk defined trades\n")
defined = sorted([r for r in D if r["risk_reward"] is not None],
                 key=lambda r: r["risk_reward"], reverse=True)[:25]
w("\nThe 25 defined-risk structures with the richest modelled reward-to-risk (low probability — a high "
  "R:R means the market must cooperate; read each full entry before trading):\n")
w("| Rank | Strategy | R:R | Max P (pts) | Max L (pts) |")
w("|---|---|---|---|---|")
for i, r in enumerate(defined, 1):
    w(f"| {i} | {r['name']} (#{r['n']}) | {r['risk_reward']:.2f} | {mp(r)} | {ml(r)} |")
w("")

w("\n## Decision table E — credit (income) structures at a glance\n")
credit = [r for r in D if r["net_cost"] < 0 and abs(r["net_cost"]) <= 3000]
w(f"\nThe {len(credit)} option-only structures that open for a NET CREDIT (premium received up front — "
  "your edge is theta and an over-priced IV that decays):\n")
w("> " + "; ".join(f"{r['name']} (#{r['n']}, credit {abs(r['net_cost']):.0f})" for r in credit) + ".\n")

BY = {r["slug"]: r for r in D}
def ref(*slugs):
    out = []
    for s in slugs:
        r = BY.get(s)
        if r:
            out.append(f"{r['name']} (#{r['n']})")
    return "; ".join(out)

# ---------------- situational playbook index ----------------
w("\n## Decision table F — the situational playbook: what to trade when you see X\n")
w("This is the table to internalise. Read the left column as *what you actually see on the screen or the "
  "calendar*, and the right column as your first-choice structures (turn to each numbered entry for the "
  "full plan). Always filter the suggestion through your own risk rule before trading.\n")
SIT = [
    ("India VIX very low (~11-12), options look cheap",
     ref("low_iv_long_calendar", "call_calendar", "long_straddle_event", "call_backspread_1x2")),
    ("India VIX high (~20+), premium is rich and fear is in the tape",
     ref("iron_condor", "high_iv_short_strangle", "jade_lizard", "bull_put_spread")),
    ("IV rank above 70 (volatility expensive vs its own year)",
     ref("iron_butterfly", "iron_condor_45d", "short_strangle_delta10", "bear_call_spread")),
    ("IV rank below 20 (volatility cheap, likely to expand)",
     ref("low_iv_long_calendar", "double_calendar", "long_strangle", "put_backspread_1x2")),
    ("Strong uptrend with shallow pullbacks to support",
     ref("trend_pullback_call_debit", "bull_call_spread_atm", "pmcc", "stock_replacement_leaps")),
    ("Strong downtrend, lower highs and lower lows",
     ref("bear_put_spread_atm", "put_diagonal", "bear_call_spread", "put_backspread_otm")),
    ("Tight coiling range, low IV, a breakout looks imminent",
     ref("range_breakout_long_strangle", "reverse_iron_condor", "long_straddle")),
    ("Quiet, well-defined range you expect to hold",
     ref("iron_condor", "long_call_butterfly", "short_strangle")),
    ("Expiry day and price is pinned near a round strike",
     ref("expiry_day_iron_fly", "atm_butterfly_pin", "monthly_expiry_butterfly")),
    ("Union Budget day ahead (large fiscal-event tail)",
     ref("budget_day_iron_condor", "reverse_iron_fly_event")),
    ("RBI policy decision in two days",
     ref("rbi_policy_calendar", "low_iv_long_calendar")),
    ("A single stock reports results tomorrow, IV is cheap",
     ref("earnings_long_straddle", "long_straddle_event")),
    ("Just after results/an event — IV is about to crush",
     ref("post_event_short_strangle", "short_straddle_45d")),
    ("Panicky gap-down on global news, you think it overshot",
     ref("gap_fade_bull_put", "bull_put_spread_narrow")),
    ("You want to buy Nifty/a stock, but lower and get paid to wait",
     ref("cash_secured_put_entry", "the_wheel")),
    ("You are long and want regular income against the position",
     ref("covered_call", "covered_strangle", "buy_write")),
    ("You are long and want cheap downside protection",
     ref("collar", "costless_collar", "put_spread_collar")),
    ("You want a budgeted crash hedge for a whole portfolio",
     ref("portfolio_tail_putspread", "tail_risk_hedge", "index_hedge_overlay")),
    ("You expect an explosive move but not the direction",
     ref("long_straddle", "reverse_iron_condor", "long_strangle")),
    ("You expect an explosive move UP specifically",
     ref("call_backspread_1x2", "slingshot_call", "risk_reversal_bull")),
    ("You expect a slow grind up and want to be paid for it",
     ref("bull_put_spread", "call_ratio_1x2", "jade_lizard")),
    ("High IV you expect to collapse toward the mean",
     ref("short_straddle_45d", "iron_butterfly", "call_calendar")),
    ("Low IV you expect to expand ahead of a catalyst",
     ref("low_iv_long_calendar", "long_straddle", "call_backspread_1x2")),
    ("You are a beginner and want DEFINED risk only",
     ref("bull_call_spread_atm", "iron_condor", "long_call_butterfly", "bear_put_spread_atm")),
    ("The put skew is very steep (downside puts richly bid)",
     ref("put_ratio_1x2", "jade_lizard", "risk_reversal_bull")),
    ("Long-term bullish but want to free up capital",
     ref("stock_replacement_leaps", "pmcc", "long_leaps_call")),
    ("Bank Nifty weekly, quiet open, you want fast theta (tiny size)",
     ref("banknifty_intraday_straddle", "iron_fly_weekly")),
    ("Mildly bullish within a range (a directional income lean)",
     ref("condor_skewed_bull", "broken_wing_put_butterfly", "bull_put_spread_wide")),
]
w("| When you see... | First-choice structures |")
w("|---|---|")
for sit, recs in SIT:
    w(f"| {sit} | {recs} |")
w("")

# ---------------- the core set ----------------
w("\n## Decision table G — the core set every Nifty trader should master first\n")
w("You do not need all 200 to be profitable. Master these dozen cold — what they are, when they win, how "
  "they lose — and you can handle almost any market the NSE throws at you. The other 188 are refinements "
  "of these core ideas.\n")
CORE = ["long_call_atm", "long_put_atm", "bull_call_spread_atm", "bear_put_spread_atm",
        "bull_put_spread", "bear_call_spread", "iron_condor", "iron_butterfly",
        "long_straddle", "covered_call", "cash_secured_put_entry", "collar"]
w("| Core strategy | View | When it is the right tool |")
w("|---|---|---|")
core_when = {
    "long_call_atm": "Convinced bullish, want leverage with capped risk and low IV.",
    "long_put_atm": "Convinced bearish or buying portfolio insurance.",
    "bull_call_spread_atm": "Moderately bullish; cheaper than a naked call.",
    "bear_put_spread_atm": "Moderately bearish with defined risk.",
    "bull_put_spread": "Neutral-to-bullish and IV is high — get paid to be patient.",
    "bear_call_spread": "Neutral-to-bearish and IV is high.",
    "iron_condor": "Range-bound with elevated IV — the workhorse income trade.",
    "iron_butterfly": "Expect a pin near ATM with rich premium to sell.",
    "long_straddle": "A big move is coming, direction unknown, and IV is cheap.",
    "covered_call": "You hold the underlying and want yield in a flat market.",
    "cash_secured_put_entry": "You want to own lower and get paid while you wait.",
    "collar": "You are long and want near-free downside protection.",
}
for s in CORE:
    r = BY[s]
    w(f"| {r['name']} (#{r['n']}) | {r['view']} | {core_when[s]} |")
w("")

# ---------------- by tenor ----------------
w("\n## Decision table H — choosing the tenor (days to expiry)\n")
w("Direction and volatility pick the family; the calendar picks the tenor. The same structure behaves "
  "very differently weekly versus monthly versus long-dated.\n")
w("| Tenor | Character | Best-suited structures |")
w("|---|---|---|")
w("| **Weekly (0-7 DTE)** | Fast theta, vicious gamma — small size, active management | "
  "Expiry-day iron fly, weekly iron condor, pin butterfly, intraday short straddle (tiny) |")
w("| **Monthly (20-45 DTE)** | The professional premium-selling window; manage at ~50% | "
  "45-DTE iron condor, iron butterfly, short strangle, credit verticals, calendars |")
w("| **Quarter / 60-90 DTE** | More vega, more room to be right; slower decay | "
  "Diagonals, double diagonals, protective collars, broken-wing flies |")
w("| **LEAPS (180-365 DTE)** | Mostly delta and vega; theta is a slow bleed | "
  "Stock-replacement LEAPS, poor-man's covered call, long-dated protective puts |")
w("")

# ---------------- family Greeks signature ----------------
w("\n## Decision table I — the Greeks signature of each family\n")
w("Before you put on any structure, know its net Greeks: they tell you what actually moves your P&L. "
  "Delta is direction, theta is the daily drip of time, vega is your exposure to a change in implied "
  "volatility, gamma is how fast your delta itself moves.\n")
w("| Family | Typical net delta | Theta | Vega | What dominates the P&L |")
w("|---|---|---|---|---|")
sig = [
    ("Single long options", "Directional (±)", "Negative (hurts)", "Positive (helps)", "Direction + a vol move; time is the enemy"),
    ("Debit verticals", "Directional (±)", "Mildly negative", "Near zero", "Direction; vega largely cancels"),
    ("Credit verticals", "Mild (±)", "Positive (helps)", "Negative", "Theta + staying on the right side of the short strike"),
    ("Long straddle/strangle", "~0 at entry", "Negative (hurts)", "Positive (helps)", "Size of the move + rising IV"),
    ("Short straddle/strangle", "~0 at entry", "Positive (helps)", "Negative", "Time + falling IV; the tail is the danger"),
    ("Butterflies (long)", "~0 near body", "Positive near body", "Negative", "Pinning the body into expiry"),
    ("Condors (iron)", "~0 in the zone", "Positive (helps)", "Negative", "Price staying in the zone; theta harvest"),
    ("Ratio spreads", "Mild directional", "Positive (helps)", "Negative", "Drift to the short strikes; the naked tail bites"),
    ("Backspreads", "Directional", "Negative (hurts)", "Positive (helps)", "A big move plus rising IV"),
    ("Calendars/diagonals", "~0 to mild", "Positive (front decay)", "Positive (helps)", "Time decay of the front + rising IV"),
    ("Covered/income", "Long (+)", "Positive (helps)", "Negative", "The underlying's direction, cushioned by premium"),
    ("Protective/hedge", "Long, floored", "Negative (carry)", "Positive (helps)", "The underlying; the hedge caps the downside"),
]
for fam, dl, th, ve, dom in sig:
    w(f"| {fam} | {dl} | {th} | {ve} | {dom} |")
w("")

# ---------------- what kills each family ----------------
w("\n## Decision table J — the one thing that kills each family\n")
w("Every structure has a single failure mode that does most of the damage. Know it before you enter.\n")
w("| Family | The killer | The defence |")
w("|---|---|---|")
kill = [
    ("Long options", "Time decay while the move never comes (and IV crush after an event).", "Buy when IV is low; give the trade time; size as a small bet."),
    ("Debit spreads", "The move stalls short of the long strike.", "Place strikes within a realistic move; take partial profits."),
    ("Credit spreads", "A fast move blows through the short strike.", "Size to the max loss; roll the untested side; stop at a multiple of the credit."),
    ("Short straddle/strangle", "A gap or trend past the breakevens — uncapped loss.", "Define the risk with wings; size tiny; hard stop at ~2x credit."),
    ("Butterflies", "Price drifts away from the body.", "Recentre by rolling; keep cost small; it is a low-probability bet."),
    ("Iron condors", "A trend that runs out of the zone; gamma near expiry.", "Manage at ~50% profit; exit by ~21 DTE; roll the tested side."),
    ("Ratio spreads", "A strong move into the naked short strikes.", "Always know where the tail is; add a wing; flatten the ratio."),
    ("Backspreads", "Quiet, range-bound markets that bleed the debit.", "Enter ahead of an expected catalyst; take the convex wing's profit."),
    ("Calendars", "A big move away from the strike, or front IV that never rises.", "Recentre; close into an IV spike; keep size modest."),
    ("Covered calls", "A crash in the underlying (premium is a thin cushion).", "Only on names you want to own; consider a collar in fear markets."),
    ("Cash-secured puts / wheel", "A collapse in the underlying after assignment.", "Sell on names you want; size to full assignment; roll down."),
    ("Hedges", "Paying for protection that expires worthless, year after year.", "Budget the cost; monetise puts after a fall; ratchet strikes up."),
]
for fam, k, dfn in kill:
    w(f"| {fam} | {k} | {dfn} |")
w("")

# ---------------- ten laws ----------------
w("\n## The ten laws of strategy selection\n")
w("1. **View, then volatility, then the calendar.** Decide direction, then whether IV is cheap or rich, "
  "then the tenor. Never skip a step.\n")
w("2. **Buy options when IV is low; sell premium when IV is high.** IV rank and India VIX are your fuel "
  "gauge — read them before you choose a side of volatility.\n")
w("3. **Define your risk until you have earned the right not to.** Beginners trade only capped-loss "
  "structures. The uncapped column is for the experienced and the well-sized.\n")
w("4. **Size to the max loss, not to the max profit.** No single trade should risk more than 1-2% of "
  "capital. The Max-loss column in this matrix is where position sizing starts.\n")
w("5. **The high-probability trade has the small reward — and vice versa.** A 0.5 risk:reward credit "
  "spread wins often; a 5:1 butterfly wins rarely. Match the trade to your edge, not your hope.\n")
w("6. **Manage winners early.** Most premium-selling structures are best closed at ~50% of max profit, "
  "well before expiry-week gamma turns on you.\n")
w("7. **Have the exit before the entry.** Write down the profit target, the stop and the time-stop "
  "*before* you place the order. The scenario table in each entry is your map.\n")
w("8. **Respect the event calendar.** Budget, RBI policy, results and expiry change which trade is right. "
  "The same structure is brilliant on Tuesday and reckless on expiry Thursday.\n")
w("9. **One structure, one reason.** If you cannot say in a sentence why this trade and not a simpler "
  "one, trade the simpler one.\n")
w("10. **Survival first.** The goal is to still be trading next year. Nine in ten retail F&O traders are "
  "not — and almost always because they ignored laws 3 and 4.\n")

w("\n## How to use this matrix in practice\n")
w("Trade from the map, not from a hunch. First fix your **view** (Table A) and your **volatility read** "
  "(Table B); the structures that appear in both lists are your candidates. Then apply your **risk rule** "
  "(Table C) — if you are still learning, stay out of the uncapped-loss column entirely and trade only "
  "defined-risk structures. Use Table D when you want a cheap, convex, low-probability bet and Table E "
  "when you want to be the seller of expensive premium. Finally, turn to the full entry (it carries the "
  "payoff diagram, the scenario P&L table and the management plan) and size the position so the Max-loss "
  "column is never more than 1–2% of your capital. That discipline — view, volatility, risk, size — is "
  "what separates the professional from the nine-in-ten who do not make it.\n")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(L))

print("written:", OUT)
print("strategies in matrix:", len(D))
print("words:", len("\n".join(L).split()))
