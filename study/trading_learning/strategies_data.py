"""
Master list of 200 option strategies for the Strategy Encyclopedia.

Each entry:  S(slug, name, category, view, vol, note, legs, span=None)
  legs = list of (kind, offset_points_from_ATM, qty, dte_days)
         kind: 'c' call, 'p' put, 's' underlying (offset ignored, dte ignored)
         qty:  +long / -short ;  ATM reference = Nifty 24000
The engine prices each leg under a mild skew and computes max P/L, breakevens, R:R.
"""

STRATEGIES = []

def S(slug, name, category, view, vol, note, legs, span=None):
    d = {"slug": slug, "name": name, "category": category, "view": view,
         "vol": vol, "note": note, "legs": legs}
    if span:
        d["span"] = span
    STRATEGIES.append(d)


# ============================================================ 1. SINGLE-LEG & STOCK (10)
C1 = "Single-Leg & Stock Combinations"
S("long_call_atm", "Long Call (ATM)", C1, "Strongly bullish", "Long vega",
  "The simplest leveraged bullish bet; defined risk, unlimited upside.",
  [("c", 0, 1, 30)])
S("long_call_otm", "Long Call (OTM Lottery)", C1, "Aggressively bullish", "Long vega",
  "Cheap far-OTM call; low cost, low probability, big payoff on a sharp rally.",
  [("c", 500, 1, 21)])
S("long_call_itm", "Long Call (Deep ITM / Stock Replacement)", C1, "Bullish", "Low vega",
  "High-delta ITM call mimics owning the index with less capital.",
  [("c", -700, 1, 60)], span=0.16)
S("long_put_atm", "Long Put (ATM)", C1, "Strongly bearish", "Long vega",
  "Leveraged bearish bet or portfolio insurance; defined risk.",
  [("p", 0, 1, 30)])
S("long_put_otm", "Long Put (OTM)", C1, "Aggressively bearish", "Long vega",
  "Cheap crash/breakdown bet; needs a real move to pay.",
  [("p", -500, 1, 21)])
S("long_put_itm", "Long Put (Deep ITM)", C1, "Bearish", "Low vega",
  "High-delta put; near 1:1 short exposure with capped risk.",
  [("p", 700, 1, 60)], span=0.16)
S("short_call_naked", "Short Call (Naked)", C1, "Bearish / neutral", "Short vega",
  "Sell premium expecting the index to stay below the strike; unlimited risk.",
  [("c", 300, -1, 30)])
S("short_put_naked", "Short Put (Naked / Cash-Secured)", C1, "Bullish / neutral", "Short vega",
  "Get paid to agree to buy lower; large but bounded downside.",
  [("p", -300, -1, 30)])
S("long_leaps_call", "Long LEAPS Call", C1, "Long-term bullish", "Long vega",
  "Long-dated call for a multi-month trend with slow theta bleed.",
  [("c", 0, 1, 365)], span=0.20)
S("long_leaps_put", "Long LEAPS Put", C1, "Long-term bearish / hedge", "Long vega",
  "Long-dated put as a strategic hedge or bearish position.",
  [("p", 0, 1, 365)], span=0.20)

# ============================================================ 2. VERTICAL SPREADS (16)
C2 = "Vertical Spreads"
S("bull_call_spread_atm", "Bull Call Spread (ATM)", C2, "Moderately bullish", "Neutral vega",
  "Buy ATM call, sell higher call; capped, cheaper than a naked call.",
  [("c", 0, 1, 30), ("c", 300, -1, 30)])
S("bull_call_spread_otm", "Bull Call Spread (OTM)", C2, "Bullish breakout", "Neutral vega",
  "Both strikes OTM; low cost, higher reward-to-risk, lower probability.",
  [("c", 200, 1, 30), ("c", 500, -1, 30)])
S("bull_call_spread_itm", "Bull Call Spread (ITM)", C2, "Bullish, high probability", "Neutral vega",
  "Deep strikes; high cost, high probability of full payout.",
  [("c", -300, 1, 30), ("c", 100, -1, 30)])
S("bear_put_spread_atm", "Bear Put Spread (ATM)", C2, "Moderately bearish", "Neutral vega",
  "Buy ATM put, sell lower put; defined-risk bearish debit spread.",
  [("p", 0, 1, 30), ("p", -300, -1, 30)])
S("bear_put_spread_otm", "Bear Put Spread (OTM)", C2, "Bearish breakdown", "Neutral vega",
  "Cheaper OTM version; needs a larger fall to pay fully.",
  [("p", -200, 1, 30), ("p", -500, -1, 30)])
S("bear_put_spread_itm", "Bear Put Spread (ITM)", C2, "Bearish, high probability", "Neutral vega",
  "Deep strikes for a high-probability bearish payout.",
  [("p", 300, 1, 30), ("p", -100, -1, 30)])
S("bull_put_spread", "Bull Put Spread (Credit)", C2, "Neutral to bullish", "Short vega",
  "Sell a put, buy a lower put; collect credit, defined risk. Income classic.",
  [("p", 0, -1, 30), ("p", -300, 1, 30)])
S("bull_put_spread_wide", "Bull Put Spread (Wide)", C2, "Neutral to bullish", "Short vega",
  "Wider strikes: more credit, more risk, lower R:R but higher max profit.",
  [("p", 0, -1, 30), ("p", -600, 1, 30)])
S("bear_call_spread", "Bear Call Spread (Credit)", C2, "Neutral to bearish", "Short vega",
  "Sell a call, buy a higher call; credit with defined risk.",
  [("c", 0, -1, 30), ("c", 300, 1, 30)])
S("bear_call_spread_wide", "Bear Call Spread (Wide)", C2, "Neutral to bearish", "Short vega",
  "Wider call credit spread; more premium, more risk.",
  [("c", 0, -1, 30), ("c", 600, 1, 30)])
S("bull_call_spread_far", "Bull Call Spread (Far OTM Cheapie)", C2, "Bullish breakout", "Neutral vega",
  "Lottery-style spread far above spot; tiny cost, large R:R.",
  [("c", 300, 1, 30), ("c", 700, -1, 30)])
S("bear_put_spread_far", "Bear Put Spread (Far OTM)", C2, "Bearish breakdown", "Neutral vega",
  "Cheap far-OTM bearish spread for a sharp drop.",
  [("p", -300, 1, 30), ("p", -700, -1, 30)])
S("bull_put_spread_narrow", "Bull Put Spread (Narrow / High Prob)", C2, "Neutral to bullish", "Short vega",
  "Tight, further-OTM credit spread: high win rate, small credit.",
  [("p", -200, -1, 30), ("p", -400, 1, 30)])
S("bear_call_spread_narrow", "Bear Call Spread (Narrow / High Prob)", C2, "Neutral to bearish", "Short vega",
  "Tight far-OTM call credit spread; high probability income.",
  [("c", 200, -1, 30), ("c", 400, 1, 30)])
S("deep_itm_bull_call", "Deep-ITM Bull Call Spread", C2, "Bullish, very high prob", "Neutral vega",
  "Near-max-probability debit spread acting like a high-delta proxy.",
  [("c", -500, 1, 30), ("c", -200, -1, 30)])
S("deep_otm_bear_call", "Deep-OTM Bear Call Spread", C2, "Mildly bearish / range", "Short vega",
  "Far-OTM call credit spread; sells the upside tail for steady income.",
  [("c", 400, -1, 30), ("c", 700, 1, 30)])

# ============================================================ 3. STRADDLES / STRANGLES (16)
C3 = "Straddles, Strangles & Volatility"
S("long_straddle", "Long Straddle", C3, "Big move, direction unknown", "Long vega",
  "Buy ATM call + put; profits on a large move either way. Theta-heavy.",
  [("c", 0, 1, 30), ("p", 0, 1, 30)])
S("short_straddle", "Short Straddle", C3, "Range-bound / falling IV", "Short vega",
  "Sell ATM call + put; max theta income, unlimited risk on a big move.",
  [("c", 0, -1, 30), ("p", 0, -1, 30)])
S("long_strangle", "Long Strangle", C3, "Big move, cheaper than straddle", "Long vega",
  "Buy OTM call + OTM put; lower cost, needs a bigger move.",
  [("c", 400, 1, 30), ("p", -400, 1, 30)])
S("short_strangle", "Short Strangle", C3, "Range-bound, high IV", "Short vega",
  "Sell OTM call + put; wide profit zone, large tail risk.",
  [("c", 400, -1, 30), ("p", -400, -1, 30)])
S("long_strangle_wide", "Long Strangle (Wide)", C3, "Very big move", "Long vega",
  "Far-OTM strangle; very cheap, needs an outsized move.",
  [("c", 700, 1, 30), ("p", -700, 1, 30)])
S("short_strangle_wide", "Short Strangle (Wide / 16-delta)", C3, "Range-bound", "Short vega",
  "Classic ~16-delta short strangle; high win rate, define or hedge the tails.",
  [("c", 700, -1, 30), ("p", -700, -1, 30)])
S("long_guts", "Long Guts", C3, "Big move", "Long vega",
  "Buy ITM call + ITM put; same shape as a strangle built from ITM options.",
  [("c", -300, 1, 30), ("p", 300, 1, 30)])
S("short_guts", "Short Guts", C3, "Range-bound", "Short vega",
  "Sell ITM call + ITM put; collects intrinsic + time value, large risk.",
  [("c", -300, -1, 30), ("p", 300, -1, 30)])
S("strip", "Strip (Bearish Straddle)", C3, "Big move, bearish bias", "Long vega",
  "1 call + 2 puts; profits on a move, twice as fast on the downside.",
  [("c", 0, 1, 30), ("p", 0, 2, 30)])
S("strap", "Strap (Bullish Straddle)", C3, "Big move, bullish bias", "Long vega",
  "2 calls + 1 put; profits on a move, twice as fast on the upside.",
  [("c", 0, 2, 30), ("p", 0, 1, 30)])
S("long_straddle_weekly", "Long Straddle (Weekly)", C3, "Big move within days", "Long vega",
  "Short-dated straddle; cheap but brutal theta — for imminent catalysts.",
  [("c", 0, 1, 7), ("p", 0, 1, 7)])
S("short_strangle_weekly", "Short Strangle (Weekly)", C3, "Quiet week", "Short vega",
  "Weekly OTM strangle harvesting fast theta; watch the gamma tail.",
  [("c", 350, -1, 7), ("p", -350, -1, 7)])
S("long_strangle_lotto", "Long Strangle (Weekly Lotto)", C3, "Explosive move", "Long vega",
  "Very cheap far-OTM weekly strangle; small bet on a violent move.",
  [("c", 700, 1, 7), ("p", -700, 1, 7)])
S("short_straddle_45d", "Short Straddle (45-DTE)", C3, "Range-bound, rich IV", "Short vega",
  "Longer-dated short straddle; slower theta but more room and management time.",
  [("c", 0, -1, 45), ("p", 0, -1, 45)])
S("long_straddle_event", "Long Straddle (Pre-Event)", C3, "Event move", "Long vega",
  "Buy the straddle into a known catalyst; beware post-event IV crush.",
  [("c", 0, 1, 5), ("p", 0, 1, 5)])
S("short_strangle_delta10", "Short Strangle (10-delta)", C3, "Strongly range-bound", "Short vega",
  "Ultra-wide short strangle; very high win rate, fat but rare tail loss.",
  [("c", 900, -1, 30), ("p", -900, -1, 30)], span=0.16)

# ============================================================ 4. BUTTERFLIES (20)
C4 = "Butterflies"
S("long_call_butterfly", "Long Call Butterfly", C4, "Pin near body strike", "Short vega",
  "Buy 1 / sell 2 / buy 1 calls; cheap, defined, max profit if spot pins the body.",
  [("c", -300, 1, 30), ("c", 0, -2, 30), ("c", 300, 1, 30)])
S("long_put_butterfly", "Long Put Butterfly", C4, "Pin near body strike", "Short vega",
  "Put-built butterfly; identical tent payoff to the call butterfly.",
  [("p", 300, 1, 30), ("p", 0, -2, 30), ("p", -300, 1, 30)])
S("short_call_butterfly", "Short Call Butterfly", C4, "Move away from body", "Long vega",
  "Reverse butterfly; small credit, profits if spot leaves the body.",
  [("c", -300, -1, 30), ("c", 0, 2, 30), ("c", 300, -1, 30)])
S("iron_butterfly", "Iron Butterfly", C4, "Pin near ATM, high IV", "Short vega",
  "Short ATM straddle + protective wings; rich credit, narrow profit tent.",
  [("c", 0, -1, 30), ("p", 0, -1, 30), ("c", 300, 1, 30), ("p", -300, 1, 30)])
S("reverse_iron_butterfly", "Reverse Iron Butterfly", C4, "Big move from ATM", "Long vega",
  "Long ATM strangle financed by short wings; defined-risk long-vol tent.",
  [("c", 0, 1, 30), ("p", 0, 1, 30), ("c", 300, -1, 30), ("p", -300, -1, 30)])
S("broken_wing_call_butterfly", "Broken-Wing Call Butterfly", C4, "Bullish pin, no upside risk", "Short vega",
  "Skip-strike fly often for a credit; removes the upside loss zone.",
  [("c", -300, 1, 30), ("c", 0, -2, 30), ("c", 500, 1, 30)])
S("broken_wing_put_butterfly", "Broken-Wing Put Butterfly", C4, "Bearish pin, no downside risk", "Short vega",
  "Skip-strike put fly; shifts/removes risk on one side, often a credit.",
  [("p", 300, 1, 30), ("p", 0, -2, 30), ("p", -500, 1, 30)])
S("skip_strike_butterfly", "Skip-Strike Butterfly (Call)", C4, "Bullish drift", "Short vega",
  "Wider upper wing; cheaper, directional tilt to the upside.",
  [("c", -200, 1, 30), ("c", 0, -2, 30), ("c", 600, 1, 30)])
S("unbalanced_butterfly", "Unbalanced (Ratio) Butterfly", C4, "Directional pin", "Short vega",
  "Uneven leg counts skew the tent and the risk toward one side.",
  [("c", -300, 1, 30), ("c", 0, -3, 30), ("c", 300, 2, 30)])
S("long_butterfly_wide", "Long Butterfly (Wide Wings)", C4, "Broad pin zone", "Short vega",
  "Wider wings widen the profit tent at a higher cost.",
  [("c", -600, 1, 30), ("c", 0, -2, 30), ("c", 600, 1, 30)], span=0.16)
S("long_butterfly_narrow", "Long Butterfly (Narrow)", C4, "Tight pin", "Short vega",
  "Tight wings: very cheap, very high reward-to-risk, low probability.",
  [("c", -150, 1, 14), ("c", 0, -2, 14), ("c", 150, 1, 14)])
S("otm_call_butterfly", "OTM Call Butterfly (Bullish Target)", C4, "Bullish to a target", "Short vega",
  "Butterfly centred above spot; pays if the index drifts to the target.",
  [("c", 200, 1, 30), ("c", 500, -2, 30), ("c", 800, 1, 30)], span=0.16)
S("otm_put_butterfly", "OTM Put Butterfly (Bearish Target)", C4, "Bearish to a target", "Short vega",
  "Butterfly centred below spot for a measured downside target.",
  [("p", -200, 1, 30), ("p", -500, -2, 30), ("p", -800, 1, 30)], span=0.16)
S("iron_butterfly_wide", "Iron Butterfly (Wide Wings)", C4, "Pin near ATM", "Short vega",
  "Wider wings: less credit, smaller max loss, broader tent.",
  [("c", 0, -1, 30), ("p", 0, -1, 30), ("c", 500, 1, 30), ("p", -500, 1, 30)], span=0.16)
S("broken_wing_iron_fly", "Broken-Wing Iron Butterfly", C4, "Neutral with a skew", "Short vega",
  "Asymmetric wings move the risk to one side for extra credit.",
  [("c", 0, -1, 30), ("p", 0, -1, 30), ("c", 300, 1, 30), ("p", -500, 1, 30)])
S("put_broken_wing_credit", "Put Broken-Wing (Income)", C4, "Neutral to bullish", "Short vega",
  "Put-side skip-strike fly taken for a credit; bullish-leaning income.",
  [("p", 200, 1, 30), ("p", -100, -2, 30), ("p", -600, 1, 30)], span=0.16)
S("iron_fly_weekly", "Iron Butterfly (Weekly)", C4, "Pin this week", "Short vega",
  "Weekly iron fly; rich theta, sharp gamma — manage actively.",
  [("c", 0, -1, 7), ("p", 0, -1, 7), ("c", 250, 1, 7), ("p", -250, 1, 7)])
S("reverse_iron_fly_event", "Reverse Iron Butterfly (Event)", C4, "Event breakout", "Long vega",
  "Defined-risk long-vol play into a catalyst week.",
  [("c", 0, 1, 7), ("p", 0, 1, 7), ("c", 300, -1, 7), ("p", -300, -1, 7)])
S("atm_butterfly_pin", "Expiry-Day Pin Butterfly", C4, "Expiry pin", "Short vega",
  "Cheap, very tight fly on expiry day betting on a max-pain pin.",
  [("c", -100, 1, 2), ("c", 0, -2, 2), ("c", 100, 1, 2)])
S("unbalanced_iron_fly", "Unbalanced Iron Butterfly", C4, "Skewed neutral", "Short vega",
  "Wings at different distances tilt the payoff and the credit.",
  [("c", 0, -1, 30), ("p", 0, -1, 30), ("c", 250, 1, 30), ("p", -600, 1, 30)], span=0.16)

# ============================================================ 5. CONDORS (16)
C5 = "Condors"
S("iron_condor", "Iron Condor", C5, "Range-bound, elevated IV", "Short vega",
  "Short OTM strangle + protective wings; the workhorse income trade.",
  [("c", 400, -1, 30), ("c", 700, 1, 30), ("p", -400, -1, 30), ("p", -700, 1, 30)], span=0.14)
S("iron_condor_wide", "Iron Condor (Wide)", C5, "Range-bound", "Short vega",
  "Wider shorts and wings: more credit, lower probability, bigger zone.",
  [("c", 600, -1, 30), ("c", 1000, 1, 30), ("p", -600, -1, 30), ("p", -1000, 1, 30)], span=0.18)
S("iron_condor_narrow", "Iron Condor (Narrow)", C5, "Tightly range-bound", "Short vega",
  "Closer shorts: bigger credit, smaller zone, higher gamma risk.",
  [("c", 250, -1, 30), ("c", 500, 1, 30), ("p", -250, -1, 30), ("p", -500, 1, 30)])
S("call_condor", "Call Condor", C5, "Range-bound", "Short vega",
  "All-call condor; same flat-topped payoff built from one option type.",
  [("c", -300, 1, 30), ("c", 0, -1, 30), ("c", 300, -1, 30), ("c", 600, 1, 30)], span=0.16)
S("put_condor", "Put Condor", C5, "Range-bound", "Short vega",
  "All-put condor; mirror of the call condor.",
  [("p", 300, 1, 30), ("p", 0, -1, 30), ("p", -300, -1, 30), ("p", -600, 1, 30)], span=0.16)
S("reverse_iron_condor", "Reverse Iron Condor", C5, "Break out of a range", "Long vega",
  "Long-vol, defined-risk condor; profits if spot leaves the body.",
  [("c", 400, 1, 30), ("c", 700, -1, 30), ("p", -400, 1, 30), ("p", -700, -1, 30)], span=0.16)
S("broken_wing_iron_condor", "Broken-Wing Iron Condor", C5, "Range with a lean", "Short vega",
  "Unequal wings move risk to one side and lift the credit.",
  [("c", 400, -1, 30), ("c", 700, 1, 30), ("p", -400, -1, 30), ("p", -900, 1, 30)], span=0.18)
S("unbalanced_iron_condor", "Unbalanced Iron Condor", C5, "Directional range", "Short vega",
  "More contracts on one side to express a mild directional bias.",
  [("c", 400, -1, 30), ("c", 700, 1, 30), ("p", -400, -2, 30), ("p", -700, 2, 30)], span=0.16)
S("iron_condor_weekly", "Iron Condor (Weekly)", C5, "Quiet week", "Short vega",
  "Weekly condor; quick theta, high gamma near expiry.",
  [("c", 300, -1, 7), ("c", 500, 1, 7), ("p", -300, -1, 7), ("p", -500, 1, 7)])
S("iron_condor_delta10", "Iron Condor (10-delta)", C5, "Strongly range-bound", "Short vega",
  "Far-OTM high-probability condor; small credit, rare large loss.",
  [("c", 800, -1, 30), ("c", 1100, 1, 30), ("p", -800, -1, 30), ("p", -1100, 1, 30)], span=0.18)
S("condor_skewed_bull", "Bullish Skewed Condor", C5, "Drift up within a range", "Short vega",
  "Condor body shifted above spot for a mild bullish lean.",
  [("c", 0, 1, 30), ("c", 300, -1, 30), ("c", 600, -1, 30), ("c", 900, 1, 30)], span=0.16)
S("condor_skewed_bear", "Bearish Skewed Condor", C5, "Drift down within a range", "Short vega",
  "Condor body shifted below spot for a mild bearish lean.",
  [("p", 0, 1, 30), ("p", -300, -1, 30), ("p", -600, -1, 30), ("p", -900, 1, 30)], span=0.16)
S("iron_condor_45d", "Iron Condor (45-DTE)", C5, "Range-bound", "Short vega",
  "The 45-day, ~16-delta condor; the textbook premium-selling tenor.",
  [("c", 500, -1, 45), ("c", 900, 1, 45), ("p", -500, -1, 45), ("p", -900, 1, 45)], span=0.18)
S("wide_call_condor", "Wide Call Condor", C5, "Broad range", "Short vega",
  "All-call condor with a wide flat top for a generous profit zone.",
  [("c", 0, 1, 30), ("c", 400, -1, 30), ("c", 700, -1, 30), ("c", 1100, 1, 30)], span=0.18)
S("reverse_iron_condor_weekly", "Reverse Iron Condor (Weekly Event)", C5, "Weekly breakout", "Long vega",
  "Defined-risk long-vol condor into a weekly catalyst.",
  [("c", 300, 1, 7), ("c", 600, -1, 7), ("p", -300, 1, 7), ("p", -600, -1, 7)])
S("iron_condor_unbalanced_credit", "Iron Condor (Credit-Skewed)", C5, "Range with put skew", "Short vega",
  "Tighter call side, wider put side to harvest index skew.",
  [("c", 350, -1, 30), ("c", 550, 1, 30), ("p", -450, -1, 30), ("p", -750, 1, 30)], span=0.16)

# ============================================================ 6. RATIO & BACKSPREADS (16)
C6 = "Ratio Spreads & Backspreads"
S("call_ratio_1x2", "Call Ratio Spread (1x2)", C6, "Mildly bullish, caps out", "Short vega",
  "Buy 1, sell 2 higher calls; cheap/credit, unlimited risk on a strong rally.",
  [("c", 0, 1, 30), ("c", 300, -2, 30)], span=0.16)
S("put_ratio_1x2", "Put Ratio Spread (1x2)", C6, "Mildly bearish, caps out", "Short vega",
  "Buy 1, sell 2 lower puts; cheap/credit, large risk on a sharp fall.",
  [("p", 0, 1, 30), ("p", -300, -2, 30)], span=0.16)
S("call_ratio_1x3", "Call Ratio Spread (1x3)", C6, "Mildly bullish", "Short vega",
  "More short calls: bigger credit, faster-rising upside risk.",
  [("c", 0, 1, 30), ("c", 400, -3, 30)], span=0.18)
S("put_ratio_1x3", "Put Ratio Spread (1x3)", C6, "Mildly bearish", "Short vega",
  "Three short puts; rich credit, heavy downside tail.",
  [("p", 0, 1, 30), ("p", -400, -3, 30)], span=0.18)
S("call_backspread_1x2", "Call Ratio Backspread (1x2)", C6, "Bullish explosive", "Long vega",
  "Sell 1, buy 2 higher calls; small risk, unlimited upside on a big rally.",
  [("c", 0, -1, 30), ("c", 300, 2, 30)], span=0.16)
S("put_backspread_1x2", "Put Ratio Backspread (1x2)", C6, "Bearish explosive", "Long vega",
  "Sell 1, buy 2 lower puts; small risk, large payoff on a crash.",
  [("p", 0, -1, 30), ("p", -300, 2, 30)], span=0.16)
S("call_backspread_1x3", "Call Ratio Backspread (1x3)", C6, "Strongly bullish", "Long vega",
  "Heavier long wing; often a credit with explosive upside.",
  [("c", 0, -1, 30), ("c", 400, 3, 30)], span=0.18)
S("put_backspread_1x3", "Put Ratio Backspread (1x3)", C6, "Strongly bearish", "Long vega",
  "Three long puts vs one short; crash insurance that can pay for itself.",
  [("p", 0, -1, 30), ("p", -400, 3, 30)], span=0.18)
S("call_ratio_credit", "Call Ratio Spread (For Credit)", C6, "Neutral to mildly bullish", "Short vega",
  "Strikes chosen for a net credit; profit zone with upside risk beyond.",
  [("c", 200, 1, 30), ("c", 450, -2, 30)], span=0.16)
S("put_ratio_credit", "Put Ratio Spread (For Credit)", C6, "Neutral to mildly bearish", "Short vega",
  "Put ratio for a credit; income with a downside tail.",
  [("p", -200, 1, 30), ("p", -450, -2, 30)], span=0.16)
S("front_ratio_call", "Front-Ratio Call Spread", C6, "Slow grind up", "Short vega",
  "Long ITM-ish call, sell 2 OTM; bullish income that caps and reverses.",
  [("c", -100, 1, 30), ("c", 250, -2, 30)], span=0.16)
S("front_ratio_put", "Front-Ratio Put Spread", C6, "Slow grind down", "Short vega",
  "Long near put, sell 2 lower; bearish income with a downside tail.",
  [("p", 100, 1, 30), ("p", -250, -2, 30)], span=0.16)
S("call_backspread_otm", "Call Backspread (OTM)", C6, "Bullish breakout", "Long vega",
  "OTM backspread; cheaper long-vol upside bet.",
  [("c", 200, -1, 30), ("c", 500, 2, 30)], span=0.16)
S("put_backspread_otm", "Put Backspread (OTM)", C6, "Bearish breakdown", "Long vega",
  "OTM put backspread; cheap defined-risk crash exposure.",
  [("p", -200, -1, 30), ("p", -500, 2, 30)], span=0.16)
S("call_ratio_2x3", "Call Ratio Spread (2x3)", C6, "Mildly bullish", "Short vega",
  "Buy 2, sell 3; a flatter ratio with a wider profit zone.",
  [("c", 0, 2, 30), ("c", 300, -3, 30)], span=0.16)
S("put_ratio_2x3", "Put Ratio Spread (2x3)", C6, "Mildly bearish", "Short vega",
  "Buy 2, sell 3 lower puts; balanced ratio income.",
  [("p", 0, 2, 30), ("p", -300, -3, 30)], span=0.16)

# ============================================================ 7. CALENDARS & DIAGONALS (18)
C7 = "Calendars & Diagonals"
S("call_calendar", "Call Calendar (Horizontal)", C7, "Pin near strike, rising IV", "Long vega",
  "Sell front call, buy same-strike back call; profits from time + vol at the strike.",
  [("c", 0, -1, 30), ("c", 0, 1, 60)])
S("put_calendar", "Put Calendar", C7, "Pin near strike", "Long vega",
  "Put-built calendar; same tent, useful with downside skew.",
  [("p", 0, -1, 30), ("p", 0, 1, 60)])
S("call_diagonal", "Call Diagonal", C7, "Bullish drift to strike", "Long vega",
  "Different strikes and expiries; a directional calendar.",
  [("c", 0, -1, 30), ("c", -300, 1, 60)], span=0.16)
S("put_diagonal", "Put Diagonal", C7, "Bearish drift to strike", "Long vega",
  "Bearish diagonal blending time and direction.",
  [("p", 0, -1, 30), ("p", 300, 1, 60)], span=0.16)
S("double_calendar", "Double Calendar", C7, "Range-bound, rising IV", "Long vega",
  "Calendars at two strikes; a wide long-vol tent around spot.",
  [("c", 300, -1, 30), ("c", 300, 1, 60), ("p", -300, -1, 30), ("p", -300, 1, 60)], span=0.16)
S("double_diagonal", "Double Diagonal", C7, "Range-bound, rising IV", "Long vega",
  "Double calendar with OTM long wings; condor-like but long vega.",
  [("c", 300, -1, 30), ("c", 500, 1, 60), ("p", -300, -1, 30), ("p", -500, 1, 60)], span=0.16)
S("pmcc", "Poor Man's Covered Call (Diagonal)", C7, "Bullish income", "Long vega",
  "Long deep-ITM LEAPS call + short front call; a capital-light covered call.",
  [("c", -1500, 1, 365), ("c", 300, -1, 30)], span=0.22)
S("pmcp", "Poor Man's Covered Put", C7, "Bearish income", "Long vega",
  "Long deep-ITM LEAPS put + short front put; capital-light covered put.",
  [("p", 1500, 1, 365), ("p", -300, -1, 30)], span=0.22)
S("reverse_calendar_call", "Reverse Call Calendar", C7, "Big move / falling IV", "Short vega",
  "Long front, short back; profits from a big move or a vol-term collapse.",
  [("c", 0, 1, 30), ("c", 0, -1, 60)])
S("reverse_calendar_put", "Reverse Put Calendar", C7, "Big move / falling IV", "Short vega",
  "Short-vega reverse calendar on the put side.",
  [("p", 0, 1, 30), ("p", 0, -1, 60)])
S("otm_call_calendar", "OTM Call Calendar (Bullish)", C7, "Drift up to strike", "Long vega",
  "Calendar placed above spot; pays if the index rises to the strike.",
  [("c", 400, -1, 30), ("c", 400, 1, 60)], span=0.16)
S("otm_put_calendar", "OTM Put Calendar (Bearish)", C7, "Drift down to strike", "Long vega",
  "Calendar below spot for a measured downside drift.",
  [("p", -400, -1, 30), ("p", -400, 1, 60)], span=0.16)
S("calendar_weekly_monthly", "Weekly-vs-Monthly Calendar", C7, "Pin near strike", "Long vega",
  "Sell weekly, buy monthly; fast front theta against a stable back leg.",
  [("c", 0, -1, 7), ("c", 0, 1, 35)])
S("pmcc_aggressive", "Aggressive Bullish Diagonal", C7, "Bullish trend", "Long vega",
  "Mid-dated ITM long call vs short OTM front; trend-following income.",
  [("c", -800, 1, 120), ("c", 200, -1, 30)], span=0.18)
S("bearish_diagonal", "Bearish Diagonal (PMCP-style)", C7, "Bearish trend", "Long vega",
  "ITM long put vs short OTM front put; bearish trend income.",
  [("p", 800, 1, 120), ("p", -200, -1, 30)], span=0.18)
S("double_calendar_wide", "Double Calendar (Wide)", C7, "Broad range, rising IV", "Long vega",
  "Wider strikes spread the long-vol tent over a larger zone.",
  [("c", 500, -1, 30), ("c", 500, 1, 60), ("p", -500, -1, 30), ("p", -500, 1, 60)], span=0.18)
S("calendar_straddle", "Calendar Straddle", C7, "Pin near ATM, rising IV", "Long vega",
  "Short front straddle + long back straddle; a powerful ATM long-vol tent.",
  [("c", 0, -1, 30), ("p", 0, -1, 30), ("c", 0, 1, 60), ("p", 0, 1, 60)])
S("calendar_45_75", "Calendar (45/75-DTE)", C7, "Pin near strike", "Long vega",
  "Longer-dated calendar; slower decay, more vega, more management room.",
  [("c", 0, -1, 45), ("c", 0, 1, 75)])

# ============================================================ 8. COVERED & INCOME (16)
C8 = "Covered & Income Strategies"
S("covered_call", "Covered Call (OTM)", C8, "Neutral to mildly bullish", "Short vega",
  "Long index + short OTM call; income that caps upside, full downside.",
  [("s", 0, 1, 0), ("c", 300, -1, 30)], span=0.16)
S("covered_call_atm", "Covered Call (ATM)", C8, "Neutral", "Short vega",
  "ATM call sold for maximum premium; caps upside immediately.",
  [("s", 0, 1, 0), ("c", 0, -1, 30)], span=0.16)
S("covered_call_deep_itm", "Covered Call (Deep ITM)", C8, "Neutral, defensive", "Short vega",
  "Deep-ITM call for a near-fixed small return and a downside cushion.",
  [("s", 0, 1, 0), ("c", -400, -1, 30)], span=0.16)
S("cash_secured_put_entry", "Cash-Secured Put (Entry)", C8, "Bullish accumulation", "Short vega",
  "Sell an OTM put to get paid while waiting to buy lower.",
  [("p", -500, -1, 30)], span=0.16)
S("the_wheel", "The Wheel", C8, "Neutral to bullish, systematic", "Short vega",
  "Cycle: sell CSP -> if assigned, sell covered calls -> repeat for steady income.",
  [("p", -400, -1, 30)], span=0.16)
S("covered_strangle", "Covered Strangle", C8, "Bullish, own the stock", "Short vega",
  "Long index + short call + short put; double premium, doubles downside.",
  [("s", 0, 1, 0), ("c", 400, -1, 30), ("p", -400, -1, 30)], span=0.16)
S("covered_combo", "Covered Combo", C8, "Bullish income", "Short vega",
  "Long index + short OTM call + short further-OTM put; tilted income.",
  [("s", 0, 1, 0), ("c", 300, -1, 30), ("p", -600, -1, 30)], span=0.16)
S("ratio_write", "Ratio Write", C8, "Neutral, range-bound", "Short vega",
  "Long index + sell 2 calls; extra premium, capped/reversing above.",
  [("s", 0, 1, 0), ("c", 200, -2, 30)], span=0.16)
S("covered_call_weekly", "Covered Call (Weekly)", C8, "Neutral", "Short vega",
  "Sell weekly calls against stock for frequent, fast-decaying income.",
  [("s", 0, 1, 0), ("c", 250, -1, 7)], span=0.16)
S("covered_put", "Covered Put", C8, "Bearish income", "Short vega",
  "Short index + short put; bearish mirror of the covered call.",
  [("s", 0, -1, 0), ("p", -300, -1, 30)], span=0.16)
S("dividend_covered_call", "Dividend-Capture Covered Call", C8, "Neutral, yield", "Short vega",
  "Hold the index for dividends and sell calls to enhance the yield.",
  [("s", 0, 1, 0), ("c", 200, -1, 45)], span=0.16)
S("short_put_ladder_income", "Short Put Ladder (Income)", C8, "Bullish accumulation", "Short vega",
  "Sell puts at two strikes to layer entry levels and premium.",
  [("p", -300, -1, 30), ("p", -600, -1, 30)], span=0.18)
S("buy_write", "Buy-Write", C8, "Neutral to mildly bullish", "Short vega",
  "Open stock and short call simultaneously as one defined income trade.",
  [("s", 0, 1, 0), ("c", 300, -1, 45)], span=0.16)
S("itm_covered_call", "In-the-Money Covered Call", C8, "Defensive income", "Short vega",
  "Slightly ITM call for higher downside protection and a fixed target.",
  [("s", 0, 1, 0), ("c", -200, -1, 30)], span=0.16)
S("cash_secured_put_weekly", "Cash-Secured Put (Weekly)", C8, "Bullish, systematic", "Short vega",
  "Weekly OTM puts harvesting quick theta while waiting to buy.",
  [("p", -250, -1, 7)], span=0.16)
S("covered_call_leaps", "Covered Call (Long-Dated)", C8, "Neutral, patient", "Short vega",
  "Sell a longer-dated call for a larger upfront premium and wider cap.",
  [("s", 0, 1, 0), ("c", 500, -1, 90)], span=0.18)

# ============================================================ 9. HEDGING & PROTECTIVE (14)
C9 = "Hedging & Protective Strategies"
S("protective_put", "Protective Put (OTM)", C9, "Bullish, insured", "Long vega",
  "Long index + long OTM put; a deductible-style floor under the position.",
  [("s", 0, 1, 0), ("p", -300, 1, 30)], span=0.16)
S("protective_put_atm", "Protective Put (ATM)", C9, "Bullish, fully insured", "Long vega",
  "ATM put for tight protection; expensive insurance, minimal downside.",
  [("s", 0, 1, 0), ("p", 0, 1, 30)], span=0.16)
S("collar", "Collar", C9, "Bullish, low-cost hedge", "Neutral vega",
  "Long index + long put + short call; cheap protection, capped upside.",
  [("s", 0, 1, 0), ("p", -300, 1, 30), ("c", 300, -1, 30)], span=0.16)
S("costless_collar", "Costless (Zero-Cost) Collar", C9, "Bullish, free hedge", "Neutral vega",
  "Strikes chosen so the short call funds the long put; range-bound payoff.",
  [("s", 0, 1, 0), ("p", -400, 1, 30), ("c", 300, -1, 30)], span=0.16)
S("put_spread_collar", "Put-Spread Collar", C9, "Bullish, cheaper hedge", "Neutral vega",
  "Finance a put spread floor by selling a call; cheaper, partial protection.",
  [("s", 0, 1, 0), ("p", -300, 1, 30), ("p", -700, -1, 30), ("c", 400, -1, 30)], span=0.16)
S("married_put", "Married Put", C9, "Bullish, protected entry", "Long vega",
  "Buy stock and put together at entry; capped risk from day one.",
  [("s", 0, 1, 0), ("p", 0, 1, 60)], span=0.16)
S("protective_collar_wide", "Wide Collar", C9, "Bullish, loose hedge", "Neutral vega",
  "Wide strikes let the position breathe while still capping the tails.",
  [("s", 0, 1, 0), ("p", -600, 1, 30), ("c", 600, -1, 30)], span=0.18)
S("fence", "Fence (Risk-Reversal Hedge)", C9, "Bullish, OTM hedge", "Neutral vega",
  "OTM put + OTM short call around a long position; a directional collar.",
  [("s", 0, 1, 0), ("p", -500, 1, 30), ("c", 500, -1, 30)], span=0.18)
S("put_ratio_hedge", "Put-Ratio Hedge", C9, "Hedge a long, cheaply", "Mixed vega",
  "Long index + 1x2 put ratio; cheap protection with a gap-risk caveat.",
  [("s", 0, 1, 0), ("p", 0, 1, 30), ("p", -600, -2, 30)], span=0.18)
S("tail_risk_hedge", "Tail-Risk Hedge", C9, "Crash insurance", "Long vega",
  "Far-OTM long puts as a small, persistent hedge against a crash.",
  [("s", 0, 1, 0), ("p", -1500, 1, 60)], span=0.20)
S("put_backspread_hedge", "Put-Backspread Hedge", C9, "Long, with crash kicker", "Long vega",
  "Overlay a put backspread so a crash turns into a gain.",
  [("s", 0, 1, 0), ("p", 0, -1, 30), ("p", -400, 2, 30)], span=0.18)
S("collar_for_credit", "Collar for a Credit", C9, "Bullish, paid to hedge", "Neutral vega",
  "Short call richer than the long put; you collect a credit to be hedged.",
  [("s", 0, 1, 0), ("p", -500, 1, 30), ("c", 200, -1, 30)], span=0.16)
S("protective_put_spread", "Protective Put Spread", C9, "Bullish, partial hedge", "Neutral vega",
  "A put spread as a cheaper but limited floor under the index.",
  [("s", 0, 1, 0), ("p", -200, 1, 30), ("p", -700, -1, 30)], span=0.16)
S("index_hedge_overlay", "Index Put Hedge Overlay", C9, "Portfolio insurance", "Long vega",
  "Buy index puts to hedge a broad long book for a fixed period.",
  [("s", 0, 1, 0), ("p", -400, 1, 45)], span=0.16)

# ============================================================ 10. SYNTHETICS & ARBITRAGE (12)
C10 = "Synthetics & Arbitrage"
S("synthetic_long_stock", "Synthetic Long Stock", C10, "Bullish (futures-like)", "Neutral vega",
  "Long call + short put same strike; replicates long index for low cost.",
  [("c", 0, 1, 30), ("p", 0, -1, 30)], span=0.16)
S("synthetic_short_stock", "Synthetic Short Stock", C10, "Bearish (futures-like)", "Neutral vega",
  "Short call + long put; replicates a short index position.",
  [("c", 0, -1, 30), ("p", 0, 1, 30)], span=0.16)
S("synthetic_long_call", "Synthetic Long Call", C10, "Bullish, insured", "Long vega",
  "Long index + long put; identical payoff to owning a call.",
  [("s", 0, 1, 0), ("p", 0, 1, 30)], span=0.16)
S("synthetic_short_call", "Synthetic Short Call", C10, "Bearish income", "Short vega",
  "Short index + short put; identical payoff to selling a call.",
  [("s", 0, -1, 0), ("p", 0, -1, 30)], span=0.16)
S("synthetic_long_put", "Synthetic Long Put", C10, "Bearish, insured", "Long vega",
  "Short index + long call; identical payoff to owning a put.",
  [("s", 0, -1, 0), ("c", 0, 1, 30)], span=0.16)
S("synthetic_short_put", "Synthetic Short Put (Covered Call)", C10, "Bullish income", "Short vega",
  "Long index + short call; identical payoff to selling a put.",
  [("s", 0, 1, 0), ("c", 0, -1, 30)], span=0.16)
S("conversion", "Conversion (Arbitrage)", C10, "Locked, rate arbitrage", "None",
  "Long stock + long put + short call; a near-riskless locked box.",
  [("s", 0, 1, 0), ("p", 0, 1, 30), ("c", 0, -1, 30)], span=0.14)
S("reversal", "Reversal (Arbitrage)", C10, "Locked, rate arbitrage", "None",
  "Short stock + short put + long call; the conversion's mirror.",
  [("s", 0, -1, 0), ("p", 0, -1, 30), ("c", 0, 1, 30)], span=0.14)
S("box_spread", "Box Spread", C10, "Locked synthetic loan", "None",
  "Bull call spread + bear put spread; a fixed payoff = a financing trade.",
  [("c", 0, 1, 30), ("c", 300, -1, 30), ("p", 300, 1, 30), ("p", 0, -1, 30)], span=0.14)
S("jelly_roll", "Jelly Roll", C10, "Calendar arbitrage", "None",
  "Long calendar in calls + short calendar in puts; isolates carry/rates.",
  [("c", 0, -1, 30), ("c", 0, 1, 60), ("p", 0, 1, 30), ("p", 0, -1, 60)], span=0.14)
S("synthetic_straddle", "Synthetic Straddle (from Stock)", C10, "Big move", "Long vega",
  "Long index + 2 long puts; reconstructs a long straddle's V-shape.",
  [("s", 0, 1, 0), ("p", 0, 2, 30)], span=0.16)
S("reverse_conversion_skew", "Reverse Conversion (Skew)", C10, "Locked, skew capture", "None",
  "An off-strike reversal capturing put-call skew mispricing.",
  [("s", 0, -1, 0), ("p", -100, -1, 30), ("c", 100, 1, 30)], span=0.14)

# ============================================================ 11. EXOTIC & NAMED COMBOS (20)
C11 = "Exotic & Named Combinations"
S("jade_lizard", "Jade Lizard", C11, "Neutral to bullish, high IV", "Short vega",
  "Short put + short call spread; no upside risk if credit > call-spread width.",
  [("p", -300, -1, 30), ("c", 300, -1, 30), ("c", 600, 1, 30)], span=0.16)
S("reverse_jade_lizard", "Reverse Jade Lizard", C11, "Neutral to bearish, high IV", "Short vega",
  "Short call + short put spread; no downside risk if credit > put-spread width.",
  [("c", 300, -1, 30), ("p", -300, -1, 30), ("p", -600, 1, 30)], span=0.16)
S("big_lizard", "Big Lizard", C11, "Neutral, high IV", "Short vega",
  "Short ATM straddle + long OTM call; removes upside risk for big credit.",
  [("c", 0, -1, 30), ("p", 0, -1, 30), ("c", 300, 1, 30)], span=0.16)
S("twisted_sister", "Twisted Sister", C11, "Neutral, high IV", "Short vega",
  "Short ATM straddle + long OTM put; removes downside risk.",
  [("c", 0, -1, 30), ("p", 0, -1, 30), ("p", -300, 1, 30)], span=0.16)
S("christmas_tree_call", "Christmas Tree Butterfly (Call)", C11, "Bullish to a target", "Short vega",
  "1-3-2 call structure; cheap directional pin with skewed wings.",
  [("c", 0, 1, 30), ("c", 300, -3, 30), ("c", 600, 2, 30)], span=0.16)
S("christmas_tree_put", "Christmas Tree Butterfly (Put)", C11, "Bearish to a target", "Short vega",
  "Put-side 1-3-2; bearish pin with an uneven payoff.",
  [("p", 0, 1, 30), ("p", -300, -3, 30), ("p", -600, 2, 30)], span=0.16)
S("zebra_call", "ZEBRA (Zero-Extrinsic Back-Ratio, Call)", C11, "Bullish, stock proxy", "Low vega",
  "Buy 2 ITM calls, sell 1 ATM; ~100 delta with little time-value bleed.",
  [("c", -400, 2, 30), ("c", 0, -1, 30)], span=0.16)
S("zebra_put", "ZEBRA (Put)", C11, "Bearish, stock proxy", "Low vega",
  "Buy 2 ITM puts, sell 1 ATM; clean short-delta proxy.",
  [("p", 400, 2, 30), ("p", 0, -1, 30)], span=0.16)
S("risk_reversal_bull", "Risk Reversal (Bullish)", C11, "Bullish", "Skew play",
  "Short OTM put funds a long OTM call; cheap/credit leveraged upside.",
  [("p", -300, -1, 30), ("c", 300, 1, 30)], span=0.16)
S("risk_reversal_bear", "Risk Reversal (Bearish)", C11, "Bearish", "Skew play",
  "Short OTM call funds a long OTM put; leveraged downside.",
  [("p", -300, 1, 30), ("c", 300, -1, 30)], span=0.16)
S("seagull_bull", "Seagull (Bullish)", C11, "Bullish, cost-reduced", "Mixed vega",
  "Bull call spread financed by a short OTM put; three-leg directional.",
  [("p", -500, -1, 30), ("c", 0, 1, 30), ("c", 400, -1, 30)], span=0.16)
S("seagull_bear", "Seagull (Bearish)", C11, "Bearish, cost-reduced", "Mixed vega",
  "Bear put spread financed by a short OTM call.",
  [("c", 500, -1, 30), ("p", 0, 1, 30), ("p", -400, -1, 30)], span=0.16)
S("batman", "Batman (Double Butterfly)", C11, "Range with twin targets", "Short vega",
  "Two OTM butterflies; a twin-peaked profile around a range.",
  [("c", 200, 1, 30), ("c", 400, -2, 30), ("c", 600, 1, 30),
   ("p", -200, 1, 30), ("p", -400, -2, 30), ("p", -600, 1, 30)], span=0.18)
S("iron_albatross", "Iron Albatross (Ultra-Wide Condor)", C11, "Broadly range-bound", "Short vega",
  "A very wide iron condor with distant wings; small credit, rare loss.",
  [("c", 700, -1, 30), ("c", 1200, 1, 30), ("p", -700, -1, 30), ("p", -1200, 1, 30)], span=0.20)
S("slingshot_call", "Slingshot (Call Backspread)", C11, "Bullish breakout", "Long vega",
  "Skewed call backspread; small/zero cost with explosive upside.",
  [("c", 100, -1, 30), ("c", 400, 2, 30)], span=0.16)
S("slingshot_put", "Slingshot (Put Backspread)", C11, "Bearish breakdown", "Long vega",
  "Skewed put backspread for a cheap crash kicker.",
  [("p", -100, -1, 30), ("p", -400, 2, 30)], span=0.16)
S("call_ratio_calendar", "Call Ratio Calendar", C11, "Pin, rising IV", "Long vega",
  "Sell 2 front calls vs 1 back; ratio'd time spread, manage the tail.",
  [("c", 0, -2, 30), ("c", 0, 1, 60)], span=0.16)
S("put_ratio_calendar", "Put Ratio Calendar", C11, "Pin, rising IV", "Long vega",
  "Put-side ratio calendar; long vega with a short-gamma caveat.",
  [("p", 0, -2, 30), ("p", 0, 1, 60)], span=0.16)
S("range_forward", "Range Forward (Zero-Cost)", C11, "Directional hedge", "Neutral vega",
  "OTM long put + OTM short call on a position; FX-style zero-cost collar.",
  [("s", 0, 1, 0), ("p", -400, 1, 30), ("c", 400, -1, 30)], span=0.18)
S("pterodactyl", "Pterodactyl (Far-Wing Condor)", C11, "Very broad range", "Short vega",
  "An even wider condor than the albatross; minimal credit, maximal zone.",
  [("c", 1000, -1, 45), ("c", 1500, 1, 45), ("p", -1000, -1, 45), ("p", -1500, 1, 45)], span=0.22)

# ============================================================ 12. PLAYBOOKS & LADDERS (26)
C12 = "Deployments, Ladders & When-to-Use Playbooks"
S("bull_call_ladder", "Bull Call Ladder", C12, "Mildly bullish, caps", "Short vega",
  "Long 1 ITM call, short 2 higher; income with upside risk beyond the top.",
  [("c", -300, 1, 30), ("c", 0, -1, 30), ("c", 300, -1, 30)], span=0.16)
S("bear_put_ladder", "Bear Put Ladder", C12, "Mildly bearish, caps", "Short vega",
  "Long 1 ITM put, short 2 lower; bearish income with a downside tail.",
  [("p", 300, 1, 30), ("p", 0, -1, 30), ("p", -300, -1, 30)], span=0.16)
S("bull_put_ladder", "Bull Put Ladder", C12, "Neutral to bullish, crash kicker", "Long vega",
  "Short 1 put, long 2 lower; credit with a profit if it crashes hard.",
  [("p", 0, -1, 30), ("p", -300, 1, 30), ("p", -600, 1, 30)], span=0.18)
S("bear_call_ladder", "Bear Call Ladder", C12, "Neutral to bearish, breakout kicker", "Long vega",
  "Short 1 call, long 2 higher; credit with upside profit on a breakout.",
  [("c", 0, -1, 30), ("c", 300, 1, 30), ("c", 600, 1, 30)], span=0.18)
S("double_iron_condor", "Double Iron Condor", C12, "Range-bound, more credit", "Short vega",
  "Two condors at different widths; layered theta with more risk.",
  [("c", 300, -1, 30), ("c", 500, 1, 30), ("p", -300, -1, 30), ("p", -500, 1, 30),
   ("c", 600, -1, 30), ("c", 800, 1, 30), ("p", -600, -1, 30), ("p", -800, 1, 30)], span=0.18)
S("weekly_expiry_short_straddle", "Expiry-Day Short Straddle", C12, "Pin on expiry", "Short vega",
  "Sell the ATM straddle on expiry day to harvest the last theta — sharp gamma.",
  [("c", 0, -1, 1), ("p", 0, -1, 1)])
S("expiry_day_iron_fly", "Expiry-Day Iron Butterfly", C12, "Pin on expiry", "Short vega",
  "Defined-risk version of the expiry pin trade.",
  [("c", 0, -1, 1), ("p", 0, -1, 1), ("c", 150, 1, 1), ("p", -150, 1, 1)])
S("gap_fade_bull_put", "Gap-Fade Bull Put Spread", C12, "Fade a gap-down", "Short vega",
  "Sell a put spread after a panicky gap down to fade the overreaction.",
  [("p", -200, -1, 5), ("p", -500, 1, 5)])
S("trend_pullback_call_debit", "Trend-Pullback Call Debit Spread", C12, "Buy the dip in an uptrend", "Neutral vega",
  "Enter a call spread on a pullback to trend support.",
  [("c", -100, 1, 21), ("c", 300, -1, 21)])
S("high_iv_short_strangle", "High-IV Short Strangle", C12, "Range-bound, IV rank > 70", "Short vega",
  "Sell premium when IV rank is high and mean reversion is the edge.",
  [("c", 600, -1, 30), ("p", -600, -1, 30)], span=0.16)
S("low_iv_long_calendar", "Low-IV Long Calendar", C12, "Pin, IV rank < 30", "Long vega",
  "Buy time spreads when IV is cheap and likely to expand.",
  [("c", 0, -1, 30), ("c", 0, 1, 60)])
S("earnings_long_straddle", "Earnings/Results Long Straddle", C12, "Stock results move", "Long vega",
  "Long straddle into a single-stock results print; mind the IV crush.",
  [("c", 0, 1, 3), ("p", 0, 1, 3)])
S("post_event_short_strangle", "Post-Event IV-Crush Short Strangle", C12, "After the news", "Short vega",
  "Sell inflated premium right after an event as IV collapses.",
  [("c", 400, -1, 7), ("p", -400, -1, 7)])
S("budget_day_iron_condor", "Budget-Day Iron Condor", C12, "Range through the Budget", "Short vega",
  "Defined-risk condor sized for a fiscal-event tail.",
  [("c", 500, -1, 4), ("c", 800, 1, 4), ("p", -500, -1, 4), ("p", -800, 1, 4)], span=0.16)
S("rbi_policy_calendar", "RBI-Policy Calendar", C12, "Pin through policy, IV pop", "Long vega",
  "Calendar into an RBI decision to play the front-month IV bid.",
  [("c", 0, -1, 2), ("c", 0, 1, 30)])
S("monthly_expiry_butterfly", "Monthly-Expiry Butterfly", C12, "Pin near max-pain", "Short vega",
  "Tight butterfly centred on the expected monthly pin.",
  [("c", -200, 1, 3), ("c", 0, -2, 3), ("c", 200, 1, 3)])
S("banknifty_intraday_straddle", "Bank Nifty Intraday Short Straddle", C12, "Quiet intraday", "Short vega",
  "Same-day ATM straddle on a high-beta index; tight stops, fast gamma.",
  [("c", 0, -1, 1), ("p", 0, -1, 1)])
S("overnight_short_strangle", "Overnight Short Strangle", C12, "Quiet close-to-open", "Short vega",
  "Sell a tight strangle into the close to capture overnight decay; gap risk.",
  [("c", 400, -1, 1), ("p", -400, -1, 1)])
S("vix_spike_put_backspread", "VIX-Spike Put Backspread", C12, "Falling market, rising vol", "Long vega",
  "Put backspread to profit from a deepening sell-off and vol expansion.",
  [("p", 0, -1, 14), ("p", -400, 2, 14)], span=0.16)
S("range_breakout_long_strangle", "Range-Breakout Long Strangle", C12, "Coiled range about to break", "Long vega",
  "Buy a strangle when a tight range and low IV precede a breakout.",
  [("c", 300, 1, 14), ("p", -300, 1, 14)])
S("theta_harvest_condor_45d", "45-DTE Theta-Harvest Condor", C12, "Range-bound, systematic", "Short vega",
  "The mechanical 45-day condor entry, managed at ~50% of max profit.",
  [("c", 600, -1, 45), ("c", 1000, 1, 45), ("p", -600, -1, 45), ("p", -1000, 1, 45)], span=0.18)
S("portfolio_collar_60d", "Portfolio Protective Collar (60-DTE)", C12, "Protect gains", "Neutral vega",
  "A longer-dated collar to ring-fence a portfolio through an uncertain quarter.",
  [("s", 0, 1, 0), ("p", -500, 1, 60), ("c", 500, -1, 60)], span=0.18)
S("stock_replacement_leaps", "Stock-Replacement LEAPS", C12, "Long-term bullish, capital-light", "Long vega",
  "Replace held index exposure with a deep-ITM LEAPS call to free capital.",
  [("c", -1500, 1, 365)], span=0.22)
S("dividend_arb_conversion", "Dividend-Arbitrage Conversion", C12, "Locked around ex-date", "None",
  "A conversion structured around a dividend to lock a small carry.",
  [("s", 0, 1, 30), ("p", 0, 1, 30), ("c", 0, -1, 30)], span=0.14)
S("pre_results_calendar", "Pre-Results Calendar", C12, "Pin into results, IV bid", "Long vega",
  "Sell the elevated front-week option vs a calmer back month before results.",
  [("c", 0, -1, 5), ("c", 0, 1, 40)])
S("portfolio_tail_putspread", "Portfolio Tail-Hedge Put Spread", C12, "Cheap crash hedge", "Long vega",
  "A far-OTM put spread as a budgeted, defined-cost portfolio crash hedge.",
  [("p", -800, 1, 60), ("p", -1500, -1, 60)], span=0.20)


if __name__ == "__main__":
    cats = {}
    for s in STRATEGIES:
        cats[s["category"]] = cats.get(s["category"], 0) + 1
    print("total strategies:", len(STRATEGIES))
    for c, n in cats.items():
        print(f"  {n:>3}  {c}")
