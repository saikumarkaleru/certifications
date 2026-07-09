# Strategy Group 13: The 200-Strategy Quick-Reference Matrix

This closing chapter is your index into the whole encyclopedia. Every figure below is computed by the same Black-Scholes engine used throughout, on Nifty at 24,000 (points per unit; multiply by the lot of about 75 for rupees). Use the master tables to scan a whole family at a glance, then the decision tables to jump straight to the structures that fit your view, your volatility read and your risk appetite. "Max profit/loss" are in points at the modelled strikes; "R:R" is reward-to-risk for defined-risk trades (a dash means one side is unlimited or undefined).

## Master matrix — all 200 strategies by family


### Group 1: Single-Leg & Stock Combinations (10)

| # | Strategy | View | Vol | Net | Max P (pts) | Max L (pts) | R:R | Breakeven(s) |
|---|---|---|---|---|---|---|---|---|
| 1 | Long Call (ATM) | Strongly bullish | Long vega | debit 456 | Unlimited | -456 | — | 24456 |
| 2 | Long Call (OTM Lottery) | Aggressively bullish | Long vega | debit 139 | Unlimited | -139 | — | 24639 |
| 3 | Long Call (Deep ITM / Stock Replacement) | Bullish | Low vega | debit 1198 | Unlimited | -1198 | — | 24498 |
| 4 | Long Put (ATM) | Strongly bearish | Long vega | debit 318 | +23681 | -318 | 74.41 | 23682 |
| 5 | Long Put (OTM) | Aggressively bearish | Long vega | debit 125 | +23374 | -125 | 186.95 | 23375 |
| 6 | Long Put (Deep ITM) | Bearish | Low vega | debit 722 | +23977 | -722 | 33.19 | 23978 |
| 7 | Short Call (Naked) | Bearish / neutral | Short vega | credit 292 | +292 | Undefined | — | 24592 |
| 8 | Short Put (Naked / Cash-Secured) | Bullish / neutral | Short vega | credit 219 | +219 | -23480 | 0.01 | 23481 |
| 9 | Long LEAPS Call | Long-term bullish | Long vega | debit 2264 | Unlimited | -2263 | — | 26263 |
| 10 | Long LEAPS Put | Long-term bearish / hedge | Long vega | debit 641 | +23358 | -641 | 36.44 | 23359 |


### Group 2: Vertical Spreads (16)

| # | Strategy | View | Vol | Net | Max P (pts) | Max L (pts) | R:R | Breakeven(s) |
|---|---|---|---|---|---|---|---|---|
| 11 | Bull Call Spread (ATM) | Moderately bullish | Neutral vega | debit 164 | +136 | -164 | 0.83 | 24164 |
| 12 | Bull Call Spread (OTM) | Bullish breakout | Neutral vega | debit 138 | +162 | -138 | 1.17 | 24338 |
| 13 | Bull Call Spread (ITM) | Bullish, high probability | Neutral vega | debit 258 | +142 | -258 | 0.55 | 23958 |
| 14 | Bear Put Spread (ATM) | Moderately bearish | Neutral vega | debit 100 | +201 | -99 | 2.02 | 23901 |
| 15 | Bear Put Spread (OTM) | Bearish breakdown | Neutral vega | debit 80 | +220 | -80 | 2.76 | 23720 |
| 16 | Bear Put Spread (ITM) | Bearish, high probability | Neutral vega | debit 171 | +229 | -171 | 1.34 | 24129 |
| 17 | Bull Put Spread (Credit) | Neutral to bullish | Short vega | credit 100 | +99 | -201 | 0.50 | 23901 |
| 18 | Bull Put Spread (Wide) | Neutral to bullish | Short vega | credit 171 | +171 | -429 | 0.40 | 23829 |
| 19 | Bear Call Spread (Credit) | Neutral to bearish | Short vega | credit 164 | +164 | -136 | 1.21 | 24164 |
| 20 | Bear Call Spread (Wide) | Neutral to bearish | Short vega | credit 289 | +289 | -311 | 0.93 | 24289 |
| 21 | Bull Call Spread (Far OTM Cheapie) | Bullish breakout | Neutral vega | debit 157 | +243 | -157 | 1.54 | 24457 |
| 22 | Bear Put Spread (Far OTM) | Bearish breakdown | Neutral vega | debit 90 | +310 | -90 | 3.45 | 23610 |
| 23 | Bull Put Spread (Narrow / High Prob) | Neutral to bullish | Short vega | credit 56 | +56 | -144 | 0.39 | 23744 |
| 24 | Bear Call Spread (Narrow / High Prob) | Neutral to bearish | Short vega | credit 96 | +97 | -103 | 0.93 | 24297 |
| 25 | Deep-ITM Bull Call Spread | Bullish, very high prob | Neutral vega | debit 218 | +82 | -218 | 0.37 | 23718 |
| 26 | Deep-OTM Bear Call Spread | Mildly bearish / range | Short vega | credit 111 | +111 | -189 | 0.59 | 24511 |


### Group 3: Straddles, Strangles & Volatility (16)

| # | Strategy | View | Vol | Net | Max P (pts) | Max L (pts) | R:R | Breakeven(s) |
|---|---|---|---|---|---|---|---|---|
| 27 | Long Straddle | Big move, direction unknown | Long vega | debit 774 | Unlimited | -766 | — | 23226, 24774 |
| 28 | Short Straddle | Range-bound / falling IV | Short vega | credit 774 | +766 | Undefined | — | 23226, 24774 |
| 29 | Long Strangle | Big move, cheaper than straddle | Long vega | debit 438 | Unlimited | -438 | — | 23162, 24838 |
| 30 | Short Strangle | Range-bound, high IV | Short vega | credit 438 | +438 | Undefined | — | 23162, 24838 |
| 31 | Long Strangle (Wide) | Very big move | Long vega | debit 264 | Unlimited | -264 | — | 23036, 24964 |
| 32 | Short Strangle (Wide / 16-delta) | Range-bound | Short vega | credit 264 | +264 | Undefined | — | 23036, 24964 |
| 33 | Long Guts | Big move | Long vega | debit 1107 | Unlimited | -507 | — | 23193, 24807 |
| 34 | Short Guts | Range-bound | Short vega | credit 1107 | +507 | Undefined | — | 23193, 24807 |
| 35 | Strip (Bearish Straddle) | Big move, bearish bias | Long vega | debit 1092 | Unlimited | -1084 | — | 23454, 25092 |
| 36 | Strap (Bullish Straddle) | Big move, bullish bias | Long vega | debit 1230 | Unlimited | -1215 | — | 22770, 24615 |
| 37 | Long Straddle (Weekly) | Big move within days | Long vega | debit 372 | Unlimited | -363 | — | 23628, 24372 |
| 38 | Short Strangle (Weekly) | Quiet week | Short vega | credit 122 | +122 | Undefined | — | 23528, 24472 |
| 39 | Long Strangle (Weekly Lotto) | Explosive move | Long vega | debit 27 | Unlimited | -27 | — | 23273, 24727 |
| 40 | Short Straddle (45-DTE) | Range-bound, rich IV | Short vega | credit 952 | +943 | Undefined | — | 23048, 24952 |
| 41 | Long Straddle (Pre-Event) | Event move | Long vega | debit 314 | Unlimited | -305 | — | 23686, 24314 |
| 42 | Short Strangle (10-delta) | Strongly range-bound | Short vega | credit 181 | +181 | Undefined | — | 22919, 25081 |


### Group 4: Butterflies (20)

| # | Strategy | View | Vol | Net | Max P (pts) | Max L (pts) | R:R | Breakeven(s) |
|---|---|---|---|---|---|---|---|---|
| 43 | Long Call Butterfly | Pin near body strike | Short vega | debit 35 | +257 | -35 | 7.38 | 23735, 24265 |
| 44 | Long Put Butterfly | Pin near body strike | Short vega | debit 35 | +257 | -35 | 7.38 | 23735, 24265 |
| 45 | Short Call Butterfly | Move away from body | Long vega | credit 35 | +35 | -257 | 0.14 | 23735, 24265 |
| 46 | Iron Butterfly | Pin near ATM, high IV | Short vega | credit 264 | +255 | -36 | 6.99 | 23736, 24264 |
| 47 | Reverse Iron Butterfly | Big move from ATM | Long vega | debit 264 | +36 | -255 | 0.14 | 23736, 24264 |
| 48 | Broken-Wing Call Butterfly | Bullish pin, no upside risk | Short vega | credit 53 | +344 | -147 | 2.34 | 24353 |
| 49 | Broken-Wing Put Butterfly | Bearish pin, no downside risk | Short vega | credit 15 | +307 | -185 | 1.66 | 23685 |
| 50 | Skip-Strike Butterfly (Call) | Bullish drift | Short vega | credit 160 | +351 | -240 | 1.46 | 24360 |
| 51 | Unbalanced (Ratio) Butterfly | Directional pin | Short vega | credit 129 | +414 | -171 | 2.42 | 24215 |
| 52 | Long Butterfly (Wide Wings) | Broad pin zone | Short vega | debit 137 | +454 | -137 | 3.31 | 23537, 24463 |
| 53 | Long Butterfly (Narrow) | Tight pin | Short vega | debit 13 | +128 | -13 | 9.72 | 23862, 24138 |
| 54 | OTM Call Butterfly (Bullish Target) | Bullish to a target | Short vega | debit 40 | +248 | -40 | 6.15 | 24240, 24760 |
| 55 | OTM Put Butterfly (Bearish Target) | Bearish to a target | Short vega | debit 24 | +272 | -24 | 11.40 | 23224, 23776 |
| 56 | Iron Butterfly (Wide Wings) | Pin near ATM | Short vega | credit 401 | +393 | -99 | 3.98 | 23599, 24401 |
| 57 | Broken-Wing Iron Butterfly | Neutral with a skew | Short vega | credit 314 | +305 | -186 | 1.64 | 23686 |
| 58 | Put Broken-Wing (Income) | Neutral to bullish | Short vega | credit 12 | +301 | -188 | 1.60 | 23588 |
| 59 | Iron Butterfly (Weekly) | Pin this week | Short vega | credit 198 | +189 | -52 | 3.64 | 23802, 24198 |
| 60 | Reverse Iron Butterfly (Event) | Event breakout | Long vega | debit 226 | +74 | -217 | 0.34 | 23774, 24226 |
| 61 | Expiry-Day Pin Butterfly | Expiry pin | Short vega | debit 16 | +76 | -16 | 4.79 | 23916, 24085 |
| 62 | Unbalanced Iron Butterfly | Skewed neutral | Short vega | credit 310 | +301 | -290 | 1.04 | 23690 |


### Group 5: Condors (16)

| # | Strategy | View | Vol | Net | Max P (pts) | Max L (pts) | R:R | Breakeven(s) |
|---|---|---|---|---|---|---|---|---|
| 63 | Iron Condor | Range-bound, elevated IV | Short vega | credit 174 | +174 | -126 | 1.39 | 23426, 24574 |
| 64 | Iron Condor (Wide) | Range-bound | Short vega | credit 167 | +167 | -233 | 0.72 | 23233, 24767 |
| 65 | Iron Condor (Narrow) | Tightly range-bound | Short vega | credit 177 | +177 | -73 | 2.42 | 23573, 24427 |
| 66 | Call Condor | Range-bound | Short vega | debit 74 | +226 | -74 | 3.05 | 23774, 24526 |
| 67 | Put Condor | Range-bound | Short vega | debit 63 | +237 | -63 | 3.76 | 23463, 24237 |
| 68 | Reverse Iron Condor | Break out of a range | Long vega | debit 174 | +126 | -174 | 0.72 | 23426, 24574 |
| 69 | Broken-Wing Iron Condor | Range with a lean | Short vega | credit 205 | +205 | -295 | 0.70 | 23395, 24605 |
| 70 | Unbalanced Iron Condor | Directional range | Short vega | credit 238 | +238 | -362 | 0.66 | 23481, 24638 |
| 71 | Iron Condor (Weekly) | Quiet week | Short vega | credit 79 | +79 | -121 | 0.65 | 23621, 24379 |
| 72 | Iron Condor (10-delta) | Strongly range-bound | Short vega | credit 98 | +98 | -202 | 0.49 | 23102, 24898 |
| 73 | Bullish Skewed Condor | Drift up within a range | Short vega | debit 79 | +221 | -79 | 2.78 | 24079, 24821 |
| 74 | Bearish Skewed Condor | Drift down within a range | Short vega | debit 50 | +250 | -50 | 5.00 | 23150, 23950 |
| 75 | Iron Condor (45-DTE) | Range-bound | Short vega | credit 229 | +229 | -171 | 1.34 | 23271, 24729 |
| 76 | Wide Call Condor | Broad range | Short vega | debit 122 | +278 | -122 | 2.28 | 24122, 24978 |
| 77 | Reverse Iron Condor (Weekly Event) | Weekly breakout | Long vega | debit 103 | +197 | -103 | 1.92 | 23597, 24403 |
| 78 | Iron Condor (Credit-Skewed) | Range with put skew | Short vega | credit 143 | +143 | -157 | 0.91 | 23407, 24493 |


### Group 6: Ratio Spreads & Backspreads (16)

| # | Strategy | View | Vol | Net | Max P (pts) | Max L (pts) | R:R | Breakeven(s) |
|---|---|---|---|---|---|---|---|---|
| 79 | Call Ratio Spread (1x2) | Mildly bullish, caps out | Short vega | credit 128 | +425 | Undefined | — | 24728 |
| 80 | Put Ratio Spread (1x2) | Mildly bearish, caps out | Short vega | credit 119 | +416 | -23280 | 0.02 | 23281 |
| 81 | Call Ratio Spread (1x3) | Mildly bullish | Short vega | credit 282 | +674 | Undefined | — | 24741 |
| 82 | Put Ratio Spread (1x3) | Mildly bearish | Short vega | credit 258 | +658 | -46540 | 0.01 | 23271 |
| 83 | Call Ratio Backspread (1x2) | Bullish explosive | Long vega | debit 128 | Unlimited | -425 | — | 24728 |
| 84 | Put Ratio Backspread (1x2) | Bearish explosive | Long vega | debit 119 | +23280 | -416 | 55.98 | 23281 |
| 85 | Call Ratio Backspread (1x3) | Strongly bullish | Long vega | debit 282 | Unlimited | -674 | — | 24741 |
| 86 | Put Ratio Backspread (1x3) | Strongly bearish | Long vega | debit 258 | +46540 | -658 | 70.74 | 23271 |
| 87 | Call Ratio Spread (For Credit) | Neutral to mildly bullish | Short vega | credit 107 | +347 | Undefined | — | 24807 |
| 88 | Put Ratio Spread (For Credit) | Neutral to mildly bearish | Short vega | credit 112 | +359 | -23187 | 0.02 | 23188 |
| 89 | Front-Ratio Call Spread | Slow grind up | Short vega | credit 115 | +463 | Undefined | — | 24715 |
| 90 | Front-Ratio Put Spread | Slow grind down | Short vega | credit 108 | +452 | -23291 | 0.02 | 23292 |
| 91 | Call Backspread (OTM) | Bullish breakout | Long vega | debit 66 | Unlimited | -355 | — | 24866 |
| 92 | Put Backspread (OTM) | Bearish breakdown | Long vega | debit 89 | +23110 | -384 | 60.15 | 23111 |
| 93 | Call Ratio Spread (2x3) | Mildly bullish | Short vega | debit 36 | +557 | Undefined | — | 24018, 24864 |
| 94 | Put Ratio Spread (2x3) | Mildly bearish | Short vega | credit 20 | +616 | -23079 | 0.03 | 23080 |


### Group 7: Calendars & Diagonals (18)

| # | Strategy | View | Vol | Net | Max P (pts) | Max L (pts) | R:R | Breakeven(s) |
|---|---|---|---|---|---|---|---|---|
| 95 | Call Calendar (Horizontal) | Pin near strike, rising IV | Long vega | debit 233 | +219 | -233 | 0.94 | 23521, 24757 |
| 96 | Put Calendar | Pin near strike | Long vega | debit 96 | +219 | -233 | 0.94 | 23523, 24752 |
| 97 | Call Diagonal | Bullish drift to strike | Long vega | debit 438 | +214 | -438 | 0.49 | 23645, 26130 |
| 98 | Put Diagonal | Bearish drift to strike | Long vega | debit 210 | +238 | -210 | 1.13 | 23067, 24545 |
| 99 | Double Calendar | Range-bound, rising IV | Long vega | debit 318 | +260 | -455 | 0.57 | 23452, 24839 |
| 100 | Double Diagonal | Range-bound, rising IV | Long vega | debit 162 | +269 | -497 | 0.54 | 23418, 24806 |
| 101 | Poor Man's Covered Call (Diagonal) | Bullish income | Long vega | debit (incl. index) | +394 | -3223 | 0.12 | 23809 |
| 102 | Poor Man's Covered Put | Bearish income | Long vega | debit 679 | +390 | -679 | 0.57 | 22733, 24584 |
| 103 | Reverse Call Calendar | Big move / falling IV | Short vega | credit 233 | +233 | -219 | 1.06 | 23521, 24757 |
| 104 | Reverse Put Calendar | Big move / falling IV | Short vega | credit 96 | +233 | -219 | 1.07 | 23523, 24752 |
| 105 | OTM Call Calendar (Bullish) | Drift up to strike | Long vega | debit 205 | +229 | -205 | 1.12 | 23890, 25271 |
| 106 | OTM Put Calendar (Bearish) | Drift down to strike | Long vega | debit 105 | +232 | -240 | 0.96 | 23098, 24372 |
| 107 | Weekly-vs-Monthly Calendar | Pin near strike | Long vega | debit 297 | +137 | -297 | 0.46 | 23719, 24396 |
| 108 | Aggressive Bullish Diagonal | Bullish trend | Long vega | debit 1327 | +309 | -1327 | 0.23 | 23789 |
| 109 | Bearish Diagonal (PMCP-style) | Bearish trend | Long vega | debit 547 | +363 | -547 | 0.66 | 24460 |
| 110 | Double Calendar (Wide) | Broad range, rising IV | Long vega | debit 300 | +202 | -434 | 0.46 | 23322, 24989 |
| 111 | Calendar Straddle | Pin near ATM, rising IV | Long vega | debit 328 | +438 | -466 | 0.94 | 23522, 24754 |
| 112 | Calendar (45/75-DTE) | Pin near strike | Long vega | debit 211 | +241 | -211 | 1.14 | 23460, 24894 |


### Group 8: Covered & Income Strategies (16)

| # | Strategy | View | Vol | Net | Max P (pts) | Max L (pts) | R:R | Breakeven(s) |
|---|---|---|---|---|---|---|---|---|
| 113 | Covered Call (OTM) | Neutral to mildly bullish | Short vega | debit (incl. index) | +592 | -23707 | 0.02 | 23708 |
| 114 | Covered Call (ATM) | Neutral | Short vega | debit (incl. index) | +456 | -23543 | 0.02 | 23544 |
| 115 | Covered Call (Deep ITM) | Neutral, defensive | Short vega | debit (incl. index) | +328 | -23271 | 0.01 | 23272 |
| 116 | Cash-Secured Put (Entry) | Bullish accumulation | Short vega | credit 169 | +169 | -23330 | 0.01 | 23331 |
| 117 | The Wheel | Neutral to bullish, systematic | Short vega | credit 192 | +192 | -23407 | 0.01 | 23408 |
| 118 | Covered Strangle | Bullish, own the stock | Short vega | debit (incl. index) | +838 | -47160 | 0.02 | 23581 |
| 119 | Covered Combo | Bullish income | Short vega | debit (incl. index) | +739 | -46959 | 0.02 | 23561 |
| 120 | Ratio Write | Neutral, range-bound | Short vega | debit (incl. index) | +884 | Undefined | — | 23315, 25085 |
| 121 | Covered Call (Weekly) | Neutral | Short vega | debit (incl. index) | +341 | -23908 | 0.01 | 23909 |
| 122 | Covered Put | Bearish income | Short vega | credit (incl. index) | +519 | Undefined | — | 24219 |
| 123 | Dividend-Capture Covered Call | Neutral, yield | Short vega | debit (incl. index) | +659 | -23540 | 0.03 | 23541 |
| 124 | Short Put Ladder (Income) | Bullish accumulation | Short vega | credit 366 | +366 | -46732 | 0.01 | 23367 |
| 125 | Buy-Write | Neutral to mildly bullish | Short vega | debit (incl. index) | +704 | -23595 | 0.03 | 23596 |
| 126 | In-the-Money Covered Call | Defensive income | Short vega | debit (incl. index) | +385 | -23414 | 0.02 | 23415 |
| 127 | Cash-Secured Put (Weekly) | Bullish, systematic | Short vega | credit 83 | +83 | -23666 | 0.00 | 23667 |
| 128 | Covered Call (Long-Dated) | Neutral, patient | Short vega | debit (incl. index) | +1073 | -23426 | 0.05 | 23427 |


### Group 9: Hedging & Protective Strategies (14)

| # | Strategy | View | Vol | Net | Max P (pts) | Max L (pts) | R:R | Breakeven(s) |
|---|---|---|---|---|---|---|---|---|
| 129 | Protective Put (OTM) | Bullish, insured | Long vega | debit (incl. index) | Unlimited | -519 | — | 24219 |
| 130 | Protective Put (ATM) | Bullish, fully insured | Long vega | debit (incl. index) | Unlimited | -318 | — | 24318 |
| 131 | Collar | Bullish, low-cost hedge | Neutral vega | debit (incl. index) | +373 | -227 | 1.64 | 23927 |
| 132 | Costless (Zero-Cost) Collar | Bullish, free hedge | Neutral vega | debit (incl. index) | +400 | -300 | 1.33 | 23900 |
| 133 | Put-Spread Collar | Bullish, cheaper hedge | Neutral vega | debit (incl. index) | +556 | -23443 | 0.02 | 23844 |
| 134 | Married Put | Bullish, protected entry | Long vega | debit (incl. index) | Unlimited | -414 | — | 24414 |
| 135 | Wide Collar | Bullish, loose hedge | Neutral vega | debit (incl. index) | +620 | -580 | 1.07 | 23980 |
| 136 | Fence (Risk-Reversal Hedge) | Bullish, OTM hedge | Neutral vega | debit (incl. index) | +536 | -464 | 1.15 | 23964 |
| 137 | Put-Ratio Hedge | Hedge a long, cheaply | Mixed vega | debit (incl. index) | Unlimited | -46821 | — | 24023 |
| 138 | Tail-Risk Hedge | Crash insurance | Long vega | debit (incl. index) | Unlimited | -1618 | — | 24118 |
| 139 | Put-Backspread Hedge | Long, with crash kicker | Long vega | debit (incl. index) | Unlimited | -866 | — | 24066 |
| 140 | Collar for a Credit | Bullish, paid to hedge | Neutral vega | debit (incl. index) | +374 | -326 | 1.15 | 23826 |
| 141 | Protective Put Spread | Bullish, partial hedge | Neutral vega | debit (incl. index) | Unlimited | -23618 | — | 24119 |
| 142 | Index Put Hedge Overlay | Portfolio insurance | Long vega | debit (incl. index) | Unlimited | -651 | — | 24251 |


### Group 10: Synthetics & Arbitrage (12)

| # | Strategy | View | Vol | Net | Max P (pts) | Max L (pts) | R:R | Breakeven(s) |
|---|---|---|---|---|---|---|---|---|
| 143 | Synthetic Long Stock | Bullish (futures-like) | Neutral vega | debit 138 | Unlimited | -24137 | — | 24138 |
| 144 | Synthetic Short Stock | Bearish (futures-like) | Neutral vega | credit 138 | +24137 | Undefined | — | 24138 |
| 145 | Synthetic Long Call | Bullish, insured | Long vega | debit (incl. index) | Unlimited | -318 | — | 24318 |
| 146 | Synthetic Short Call | Bearish income | Short vega | credit (incl. index) | +318 | Undefined | — | 24318 |
| 147 | Synthetic Long Put | Bearish, insured | Long vega | credit (incl. index) | +23543 | -456 | 51.64 | 23544 |
| 148 | Synthetic Short Put (Covered Call) | Bullish income | Short vega | debit (incl. index) | +456 | -23543 | 0.02 | 23544 |
| 149 | Conversion (Arbitrage) | Locked, rate arbitrage | None | debit (incl. index) | +138 | +138 | 1.00 | — |
| 150 | Reversal (Arbitrage) | Locked, rate arbitrage | None | credit (incl. index) | -138 | -138 | 1.00 | — |
| 151 | Box Spread | Locked synthetic loan | None | debit 298 | +2 | +2 | 1.00 | — |
| 152 | Jelly Roll | Calendar arbitrage | None | debit 137 | +1 | +1 | 1.00 | — |
| 153 | Synthetic Straddle (from Stock) | Big move | Long vega | debit (incl. index) | Unlimited | -628 | — | 23363, 24637 |
| 154 | Reverse Conversion (Skew) | Locked, skew capture | None | credit (incl. index) | -16 | -216 | 0.07 | — |


### Group 11: Exotic & Named Combinations (20)

| # | Strategy | View | Vol | Net | Max P (pts) | Max L (pts) | R:R | Breakeven(s) |
|---|---|---|---|---|---|---|---|---|
| 155 | Jade Lizard | Neutral to bullish, high IV | Short vega | credit 343 | +343 | -23356 | 0.01 | 23357 |
| 156 | Reverse Jade Lizard | Neutral to bearish, high IV | Short vega | credit 363 | +363 | Undefined | — | 24663 |
| 157 | Big Lizard | Neutral, high IV | Short vega | credit 482 | +474 | -23517 | 0.02 | 23518 |
| 158 | Twisted Sister | Neutral, high IV | Short vega | credit 555 | +547 | Undefined | — | 24555 |
| 159 | Christmas Tree Butterfly (Call) | Bullish to a target | Short vega | credit 85 | +382 | -215 | 1.78 | 24493 |
| 160 | Christmas Tree Butterfly (Put) | Bearish to a target | Short vega | credit 43 | +336 | -257 | 1.31 | 23529 |
| 161 | ZEBRA (Zero-Extrinsic Back-Ratio, Call) | Bullish, stock proxy | Low vega | debit 999 | Unlimited | -999 | — | 24199 |
| 162 | ZEBRA (Put) | Bearish, stock proxy | Low vega | debit 694 | +24106 | -693 | 34.76 | 24053 |
| 163 | Risk Reversal (Bullish) | Bullish | Skew play | debit 73 | Unlimited | -23772 | — | 24373 |
| 164 | Risk Reversal (Bearish) | Bearish | Skew play | credit 73 | +23772 | Undefined | — | 24373 |
| 165 | Seagull (Bullish) | Bullish, cost-reduced | Mixed vega | debit 42 | +358 | -23541 | 0.02 | 24042 |
| 166 | Seagull (Bearish) | Bearish, cost-reduced | Mixed vega | credit 78 | +478 | Undefined | — | 24578 |
| 167 | Batman (Double Butterfly) | Range with twin targets | Short vega | debit 30 | +170 | -29 | 5.76 | 23429, 23771, 24229, 24571 |
| 168 | Iron Albatross (Ultra-Wide Condor) | Broadly range-bound | Short vega | credit 166 | +166 | -334 | 0.50 | 23134, 24866 |
| 169 | Slingshot (Call Backspread) | Bullish breakout | Long vega | debit 95 | Unlimited | -387 | — | 24795 |
| 170 | Slingshot (Put Backspread) | Bearish breakdown | Long vega | debit 103 | +23196 | -402 | 57.65 | 23197 |
| 171 | Call Ratio Calendar | Pin, rising IV | Long vega | credit 223 | +671 | Undefined | — | 24508 |
| 172 | Put Ratio Calendar | Pin, rising IV | Long vega | credit 222 | +537 | -23914 | 0.02 | 23637 |
| 173 | Range Forward (Zero-Cost) | Directional hedge | Neutral vega | debit (incl. index) | +454 | -346 | 1.31 | 23946 |
| 174 | Pterodactyl (Far-Wing Condor) | Very broad range | Short vega | credit 146 | +146 | -354 | 0.41 | 22854, 25146 |


### Group 12: Deployments, Ladders & When-to-Use Playbooks (26)

| # | Strategy | View | Vol | Net | Max P (pts) | Max L (pts) | R:R | Breakeven(s) |
|---|---|---|---|---|---|---|---|---|
| 175 | Bull Call Ladder | Mildly bullish, caps | Short vega | credit 93 | +393 | Undefined | — | 24693 |
| 176 | Bear Put Ladder | Mildly bearish, caps | Short vega | credit 84 | +385 | -23314 | 0.02 | 23315 |
| 177 | Bull Put Ladder | Neutral to bullish, crash kicker | Long vega | debit 48 | +23051 | -348 | 66.22 | 23052 |
| 178 | Bear Call Ladder | Neutral to bearish, breakout kicker | Long vega | debit 3 | Unlimited | -303 | — | 24903 |
| 179 | Double Iron Condor | Range-bound, more credit | Short vega | credit 234 | +234 | -166 | 1.40 | 23366, 24634 |
| 180 | Expiry-Day Short Straddle | Pin on expiry | Short vega | credit 140 | +132 | Undefined | — | 23860, 24140 |
| 181 | Expiry-Day Iron Butterfly | Pin on expiry | Short vega | credit 102 | +93 | -48 | 1.94 | 23898, 24102 |
| 182 | Gap-Fade Bull Put Spread | Fade a gap-down | Short vega | credit 52 | +52 | -248 | 0.21 | 23748 |
| 183 | Trend-Pullback Call Debit Spread | Buy the dip in an uptrend | Neutral vega | debit 216 | +184 | -216 | 0.85 | 24116 |
| 184 | High-IV Short Strangle | Range-bound, IV rank > 70 | Short vega | credit 315 | +315 | Undefined | — | 23085, 24915 |
| 185 | Low-IV Long Calendar | Pin, IV rank < 30 | Long vega | debit 233 | +219 | -233 | 0.94 | 23521, 24757 |
| 186 | Earnings/Results Long Straddle | Stock results move | Long vega | debit 243 | Unlimited | -235 | — | 23757, 24243 |
| 187 | Post-Event IV-Crush Short Strangle | After the news | Short vega | credit 100 | +101 | Undefined | — | 23499, 24501 |
| 188 | Budget-Day Iron Condor | Range through the Budget | Short vega | credit 22 | +21 | -279 | 0.08 | 23479, 24521 |
| 189 | RBI-Policy Calendar | Pin through policy, IV pop | Long vega | debit 352 | +82 | -352 | 0.23 | 23837, 24220 |
| 190 | Monthly-Expiry Butterfly | Pin near max-pain | Short vega | debit 50 | +141 | -50 | 2.80 | 23850, 24150 |
| 191 | Bank Nifty Intraday Short Straddle | Quiet intraday | Short vega | credit 140 | +132 | Undefined | — | 23860, 24140 |
| 192 | Overnight Short Strangle | Quiet close-to-open | Short vega | credit 1 | +1 | Undefined | — | 23599, 24395 |
| 193 | VIX-Spike Put Backspread | Falling market, rising vol | Long vega | credit 22 | +23221 | -378 | 61.45 | 23222, 23978 |
| 194 | Range-Breakout Long Strangle | Coiled range about to break | Long vega | debit 280 | Unlimited | -280 | — | 23420, 24580 |
| 195 | 45-DTE Theta-Harvest Condor | Range-bound, systematic | Short vega | credit 206 | +206 | -194 | 1.07 | 23194, 24806 |
| 196 | Portfolio Protective Collar (60-DTE) | Protect gains | Neutral vega | debit (incl. index) | +626 | -374 | 1.67 | 23874 |
| 197 | Stock-Replacement LEAPS | Long-term bullish, capital-light | Long vega | debit (incl. index) | Unlimited | -3514 | — | 26014 |
| 198 | Dividend-Arbitrage Conversion | Locked around ex-date | None | debit (incl. index) | +138 | +138 | 1.00 | — |
| 199 | Pre-Results Calendar | Pin into results, IV bid | Long vega | debit 371 | +124 | -371 | 0.33 | 23756, 24349 |
| 200 | Portfolio Tail-Hedge Put Spread | Cheap crash hedge | Long vega | debit 95 | +605 | -95 | 6.38 | 23105 |


## Decision table A — by directional view


**Bullish** — 58 structures:

> Long Call (ATM) (#1); Long Call (OTM Lottery) (#2); Long Call (Deep ITM / Stock Replacement) (#3); Short Put (Naked / Cash-Secured) (#8); Long LEAPS Call (#9); Bull Call Spread (ATM) (#11); Bull Call Spread (OTM) (#12); Bull Call Spread (ITM) (#13); Bull Put Spread (Credit) (#17); Bull Put Spread (Wide) (#18); Bull Call Spread (Far OTM Cheapie) (#21); Bull Put Spread (Narrow / High Prob) (#23); Deep-ITM Bull Call Spread (#25); Strap (Bullish Straddle) (#36); Broken-Wing Call Butterfly (#48); Skip-Strike Butterfly (Call) (#50); OTM Call Butterfly (Bullish Target) (#54); Put Broken-Wing (Income) (#58); Call Ratio Spread (1x2) (#79); Call Ratio Spread (1x3) (#81); Call Ratio Backspread (1x2) (#83); Call Ratio Backspread (1x3) (#85); Call Ratio Spread (For Credit) (#87); Call Backspread (OTM) (#91); Call Ratio Spread (2x3) (#93); Call Diagonal (#97); Poor Man's Covered Call (Diagonal) (#101); Aggressive Bullish Diagonal (#108); Covered Call (OTM) (#113); Cash-Secured Put (Entry) (#116); The Wheel (#117); Covered Strangle (#118); Covered Combo (#119); Short Put Ladder (Income) (#124); Buy-Write (#125); Cash-Secured Put (Weekly) (#127); Protective Put (OTM) (#129); Protective Put (ATM) (#130); Collar (#131); Costless (Zero-Cost) Collar (#132); Put-Spread Collar (#133); Married Put (#134); Wide Collar (#135); Fence (Risk-Reversal Hedge) (#136); Collar for a Credit (#140); Protective Put Spread (#141); Synthetic Long Stock (#143); Synthetic Long Call (#145); Synthetic Short Put (Covered Call) (#148); Jade Lizard (#155); Christmas Tree Butterfly (Call) (#159); ZEBRA (Zero-Extrinsic Back-Ratio, Call) (#161); Risk Reversal (Bullish) (#163); Seagull (Bullish) (#165); Slingshot (Call Backspread) (#169); Bull Call Ladder (#175); Bull Put Ladder (#177); Stock-Replacement LEAPS (#197).


**Bearish** — 38 structures:

> Long Put (ATM) (#4); Long Put (OTM) (#5); Long Put (Deep ITM) (#6); Short Call (Naked) (#7); Long LEAPS Put (#10); Bear Put Spread (ATM) (#14); Bear Put Spread (OTM) (#15); Bear Put Spread (ITM) (#16); Bear Call Spread (Credit) (#19); Bear Call Spread (Wide) (#20); Bear Put Spread (Far OTM) (#22); Bear Call Spread (Narrow / High Prob) (#24); Deep-OTM Bear Call Spread (#26); Strip (Bearish Straddle) (#35); Broken-Wing Put Butterfly (#49); OTM Put Butterfly (Bearish Target) (#55); Put Ratio Spread (1x2) (#80); Put Ratio Spread (1x3) (#82); Put Ratio Backspread (1x2) (#84); Put Ratio Backspread (1x3) (#86); Put Ratio Spread (For Credit) (#88); Put Backspread (OTM) (#92); Put Ratio Spread (2x3) (#94); Put Diagonal (#98); Poor Man's Covered Put (#102); Bearish Diagonal (PMCP-style) (#109); Covered Put (#122); Synthetic Short Stock (#144); Synthetic Short Call (#146); Synthetic Long Put (#147); Reverse Jade Lizard (#156); Christmas Tree Butterfly (Put) (#160); ZEBRA (Put) (#162); Risk Reversal (Bearish) (#164); Seagull (Bearish) (#166); Slingshot (Put Backspread) (#170); Bear Put Ladder (#176); Bear Call Ladder (#178).


**Neutral / range-bound** — 84 structures:

> Short Call (Naked) (#7); Short Put (Naked / Cash-Secured) (#8); Bull Put Spread (Credit) (#17); Bull Put Spread (Wide) (#18); Bear Call Spread (Credit) (#19); Bear Call Spread (Wide) (#20); Bull Put Spread (Narrow / High Prob) (#23); Bear Call Spread (Narrow / High Prob) (#24); Deep-OTM Bear Call Spread (#26); Short Straddle (#28); Short Strangle (#30); Short Strangle (Wide / 16-delta) (#32); Short Guts (#34); Short Straddle (45-DTE) (#40); Short Strangle (10-delta) (#42); Long Call Butterfly (#43); Long Put Butterfly (#44); Iron Butterfly (#46); Broken-Wing Call Butterfly (#48); Broken-Wing Put Butterfly (#49); Unbalanced (Ratio) Butterfly (#51); Long Butterfly (Wide Wings) (#52); Long Butterfly (Narrow) (#53); Iron Butterfly (Wide Wings) (#56); Broken-Wing Iron Butterfly (#57); Put Broken-Wing (Income) (#58); Iron Butterfly (Weekly) (#59); Expiry-Day Pin Butterfly (#61); Unbalanced Iron Butterfly (#62); Iron Condor (#63); Iron Condor (Wide) (#64); Iron Condor (Narrow) (#65); Call Condor (#66); Put Condor (#67); Reverse Iron Condor (#68); Broken-Wing Iron Condor (#69); Unbalanced Iron Condor (#70); Iron Condor (10-delta) (#72); Bullish Skewed Condor (#73); Bearish Skewed Condor (#74); Iron Condor (45-DTE) (#75); Wide Call Condor (#76); Iron Condor (Credit-Skewed) (#78); Call Ratio Spread (For Credit) (#87); Put Ratio Spread (For Credit) (#88); Call Calendar (Horizontal) (#95); Put Calendar (#96); Double Calendar (#99); Double Diagonal (#100); Weekly-vs-Monthly Calendar (#107); Double Calendar (Wide) (#110); Calendar Straddle (#111); Calendar (45/75-DTE) (#112); Covered Call (OTM) (#113); Covered Call (ATM) (#114); Covered Call (Deep ITM) (#115); The Wheel (#117); Ratio Write (#120); Covered Call (Weekly) (#121); Dividend-Capture Covered Call (#123); Buy-Write (#125); Covered Call (Long-Dated) (#128); Jade Lizard (#155); Reverse Jade Lizard (#156); Big Lizard (#157); Twisted Sister (#158); Batman (Double Butterfly) (#167); Iron Albatross (Ultra-Wide Condor) (#168); Call Ratio Calendar (#171); Put Ratio Calendar (#172); Pterodactyl (Far-Wing Condor) (#174); Bull Put Ladder (#177); Bear Call Ladder (#178); Double Iron Condor (#179); Expiry-Day Short Straddle (#180); Expiry-Day Iron Butterfly (#181); High-IV Short Strangle (#184); Low-IV Long Calendar (#185); Budget-Day Iron Condor (#188); RBI-Policy Calendar (#189); Monthly-Expiry Butterfly (#190); Range-Breakout Long Strangle (#194); 45-DTE Theta-Harvest Condor (#195); Pre-Results Calendar (#199).


**Expecting a big move / breakout** — 22 structures:

> Bull Call Spread (OTM) (#12); Bull Call Spread (Far OTM Cheapie) (#21); Long Straddle (#27); Long Strangle (#29); Long Strangle (Wide) (#31); Long Guts (#33); Strip (Bearish Straddle) (#35); Strap (Bullish Straddle) (#36); Long Straddle (Weekly) (#37); Long Strangle (Weekly Lotto) (#39); Long Straddle (Pre-Event) (#41); Short Call Butterfly (#45); Reverse Iron Butterfly (#47); Reverse Iron Butterfly (Event) (#60); Reverse Iron Condor (Weekly Event) (#77); Call Backspread (OTM) (#91); Reverse Call Calendar (#103); Reverse Put Calendar (#104); Synthetic Straddle (from Stock) (#153); Slingshot (Call Backspread) (#169); Bear Call Ladder (#178); Earnings/Results Long Straddle (#186).


## Decision table B — by volatility posture


**Long volatility / vega (buy when IV is LOW)** — 65 structures:

> Long Call (ATM) (#1); Long Call (OTM Lottery) (#2); Long Put (ATM) (#4); Long Put (OTM) (#5); Long LEAPS Call (#9); Long LEAPS Put (#10); Long Straddle (#27); Long Strangle (#29); Long Strangle (Wide) (#31); Long Guts (#33); Strip (Bearish Straddle) (#35); Strap (Bullish Straddle) (#36); Long Straddle (Weekly) (#37); Long Strangle (Weekly Lotto) (#39); Long Straddle (Pre-Event) (#41); Short Call Butterfly (#45); Reverse Iron Butterfly (#47); Reverse Iron Butterfly (Event) (#60); Reverse Iron Condor (#68); Reverse Iron Condor (Weekly Event) (#77); Call Ratio Backspread (1x2) (#83); Put Ratio Backspread (1x2) (#84); Call Ratio Backspread (1x3) (#85); Put Ratio Backspread (1x3) (#86); Call Backspread (OTM) (#91); Put Backspread (OTM) (#92); Call Calendar (Horizontal) (#95); Put Calendar (#96); Call Diagonal (#97); Put Diagonal (#98); Double Calendar (#99); Double Diagonal (#100); Poor Man's Covered Call (Diagonal) (#101); Poor Man's Covered Put (#102); OTM Call Calendar (Bullish) (#105); OTM Put Calendar (Bearish) (#106); Weekly-vs-Monthly Calendar (#107); Aggressive Bullish Diagonal (#108); Bearish Diagonal (PMCP-style) (#109); Double Calendar (Wide) (#110); Calendar Straddle (#111); Calendar (45/75-DTE) (#112); Protective Put (OTM) (#129); Protective Put (ATM) (#130); Married Put (#134); Tail-Risk Hedge (#138); Put-Backspread Hedge (#139); Index Put Hedge Overlay (#142); Synthetic Long Call (#145); Synthetic Long Put (#147); Synthetic Straddle (from Stock) (#153); Slingshot (Call Backspread) (#169); Slingshot (Put Backspread) (#170); Call Ratio Calendar (#171); Put Ratio Calendar (#172); Bull Put Ladder (#177); Bear Call Ladder (#178); Low-IV Long Calendar (#185); Earnings/Results Long Straddle (#186); RBI-Policy Calendar (#189); VIX-Spike Put Backspread (#193); Range-Breakout Long Strangle (#194); Stock-Replacement LEAPS (#197); Pre-Results Calendar (#199); Portfolio Tail-Hedge Put Spread (#200).


**Short volatility / vega (sell when IV is HIGH)** — 99 structures:

> Short Call (Naked) (#7); Short Put (Naked / Cash-Secured) (#8); Bull Put Spread (Credit) (#17); Bull Put Spread (Wide) (#18); Bear Call Spread (Credit) (#19); Bear Call Spread (Wide) (#20); Bull Put Spread (Narrow / High Prob) (#23); Bear Call Spread (Narrow / High Prob) (#24); Deep-OTM Bear Call Spread (#26); Short Straddle (#28); Short Strangle (#30); Short Strangle (Wide / 16-delta) (#32); Short Guts (#34); Short Strangle (Weekly) (#38); Short Straddle (45-DTE) (#40); Short Strangle (10-delta) (#42); Long Call Butterfly (#43); Long Put Butterfly (#44); Iron Butterfly (#46); Broken-Wing Call Butterfly (#48); Broken-Wing Put Butterfly (#49); Skip-Strike Butterfly (Call) (#50); Unbalanced (Ratio) Butterfly (#51); Long Butterfly (Wide Wings) (#52); Long Butterfly (Narrow) (#53); OTM Call Butterfly (Bullish Target) (#54); OTM Put Butterfly (Bearish Target) (#55); Iron Butterfly (Wide Wings) (#56); Broken-Wing Iron Butterfly (#57); Put Broken-Wing (Income) (#58); Iron Butterfly (Weekly) (#59); Expiry-Day Pin Butterfly (#61); Unbalanced Iron Butterfly (#62); Iron Condor (#63); Iron Condor (Wide) (#64); Iron Condor (Narrow) (#65); Call Condor (#66); Put Condor (#67); Broken-Wing Iron Condor (#69); Unbalanced Iron Condor (#70); Iron Condor (Weekly) (#71); Iron Condor (10-delta) (#72); Bullish Skewed Condor (#73); Bearish Skewed Condor (#74); Iron Condor (45-DTE) (#75); Wide Call Condor (#76); Iron Condor (Credit-Skewed) (#78); Call Ratio Spread (1x2) (#79); Put Ratio Spread (1x2) (#80); Call Ratio Spread (1x3) (#81); Put Ratio Spread (1x3) (#82); Call Ratio Spread (For Credit) (#87); Put Ratio Spread (For Credit) (#88); Front-Ratio Call Spread (#89); Front-Ratio Put Spread (#90); Call Ratio Spread (2x3) (#93); Put Ratio Spread (2x3) (#94); Reverse Call Calendar (#103); Reverse Put Calendar (#104); Covered Call (OTM) (#113); Covered Call (ATM) (#114); Covered Call (Deep ITM) (#115); Cash-Secured Put (Entry) (#116); The Wheel (#117); Covered Strangle (#118); Covered Combo (#119); Ratio Write (#120); Covered Call (Weekly) (#121); Covered Put (#122); Dividend-Capture Covered Call (#123); Short Put Ladder (Income) (#124); Buy-Write (#125); In-the-Money Covered Call (#126); Cash-Secured Put (Weekly) (#127); Covered Call (Long-Dated) (#128); Synthetic Short Call (#146); Synthetic Short Put (Covered Call) (#148); Jade Lizard (#155); Reverse Jade Lizard (#156); Big Lizard (#157); Twisted Sister (#158); Christmas Tree Butterfly (Call) (#159); Christmas Tree Butterfly (Put) (#160); Batman (Double Butterfly) (#167); Iron Albatross (Ultra-Wide Condor) (#168); Pterodactyl (Far-Wing Condor) (#174); Bull Call Ladder (#175); Bear Put Ladder (#176); Double Iron Condor (#179); Expiry-Day Short Straddle (#180); Expiry-Day Iron Butterfly (#181); Gap-Fade Bull Put Spread (#182); High-IV Short Strangle (#184); Post-Event IV-Crush Short Strangle (#187); Budget-Day Iron Condor (#188); Monthly-Expiry Butterfly (#190); Bank Nifty Intraday Short Straddle (#191); Overnight Short Strangle (#192); 45-DTE Theta-Harvest Condor (#195).


**Vega-light / direction- or skew-driven** — 36 structures:

> Long Call (Deep ITM / Stock Replacement) (#3); Long Put (Deep ITM) (#6); Bull Call Spread (ATM) (#11); Bull Call Spread (OTM) (#12); Bull Call Spread (ITM) (#13); Bear Put Spread (ATM) (#14); Bear Put Spread (OTM) (#15); Bear Put Spread (ITM) (#16); Bull Call Spread (Far OTM Cheapie) (#21); Bear Put Spread (Far OTM) (#22); Deep-ITM Bull Call Spread (#25); Collar (#131); Costless (Zero-Cost) Collar (#132); Put-Spread Collar (#133); Wide Collar (#135); Fence (Risk-Reversal Hedge) (#136); Put-Ratio Hedge (#137); Collar for a Credit (#140); Protective Put Spread (#141); Synthetic Long Stock (#143); Synthetic Short Stock (#144); Conversion (Arbitrage) (#149); Reversal (Arbitrage) (#150); Box Spread (#151); Jelly Roll (#152); Reverse Conversion (Skew) (#154); ZEBRA (Zero-Extrinsic Back-Ratio, Call) (#161); ZEBRA (Put) (#162); Risk Reversal (Bullish) (#163); Risk Reversal (Bearish) (#164); Seagull (Bullish) (#165); Seagull (Bearish) (#166); Range Forward (Zero-Cost) (#173); Trend-Pullback Call Debit Spread (#183); Portfolio Protective Collar (60-DTE) (#196); Dividend-Arbitrage Conversion (#198).


## Decision table C — defined risk vs undefined (uncapped) risk


**Truly uncapped loss — size tiny, always define or hedge the tail:**

> Short Call (Naked) (#7); Short Straddle (#28); Short Strangle (#30); Short Strangle (Wide / 16-delta) (#32); Short Guts (#34); Short Strangle (Weekly) (#38); Short Straddle (45-DTE) (#40); Short Strangle (10-delta) (#42); Call Ratio Spread (1x2) (#79); Call Ratio Spread (1x3) (#81); Call Ratio Spread (For Credit) (#87); Front-Ratio Call Spread (#89); Call Ratio Spread (2x3) (#93); Ratio Write (#120); Covered Put (#122); Synthetic Short Stock (#144); Synthetic Short Call (#146); Reverse Jade Lizard (#156); Twisted Sister (#158); Risk Reversal (Bearish) (#164); Seagull (Bearish) (#166); Call Ratio Calendar (#171); Bull Call Ladder (#175); Expiry-Day Short Straddle (#180); High-IV Short Strangle (#184); Post-Event IV-Crush Short Strangle (#187); Bank Nifty Intraday Short Straddle (#191); Overnight Short Strangle (#192).


**"Bounded but catastrophic" — the worst case assumes the index falls to zero (naked-put / stock-owning trades). Manage long before that:**

> Short Put (Naked / Cash-Secured) (#8); Put Ratio Spread (1x2) (#80); Put Ratio Spread (1x3) (#82); Put Ratio Spread (For Credit) (#88); Front-Ratio Put Spread (#90); Put Ratio Spread (2x3) (#94); Covered Call (OTM) (#113); Covered Call (ATM) (#114); Covered Call (Deep ITM) (#115); Cash-Secured Put (Entry) (#116); The Wheel (#117); Covered Strangle (#118); Covered Combo (#119); Covered Call (Weekly) (#121); Dividend-Capture Covered Call (#123); Short Put Ladder (Income) (#124); Buy-Write (#125); In-the-Money Covered Call (#126); Cash-Secured Put (Weekly) (#127); Covered Call (Long-Dated) (#128); Put-Spread Collar (#133); Put-Ratio Hedge (#137); Protective Put Spread (#141); Synthetic Long Stock (#143); Synthetic Short Put (Covered Call) (#148); Jade Lizard (#155); Big Lizard (#157); Risk Reversal (Bullish) (#163); Seagull (Bullish) (#165); Put Ratio Calendar (#172); Bear Put Ladder (#176).


## Decision table D — highest reward-to-risk defined trades


The 25 defined-risk structures with the richest modelled reward-to-risk (low probability — a high R:R means the market must cooperate; read each full entry before trading):

| Rank | Strategy | R:R | Max P (pts) | Max L (pts) |
|---|---|---|---|---|
| 1 | Long Put (OTM) (#5) | 186.95 | +23374 | -125 |
| 2 | Long Put (ATM) (#4) | 74.41 | +23681 | -318 |
| 3 | Put Ratio Backspread (1x3) (#86) | 70.74 | +46540 | -658 |
| 4 | Bull Put Ladder (#177) | 66.22 | +23051 | -348 |
| 5 | VIX-Spike Put Backspread (#193) | 61.45 | +23221 | -378 |
| 6 | Put Backspread (OTM) (#92) | 60.15 | +23110 | -384 |
| 7 | Slingshot (Put Backspread) (#170) | 57.65 | +23196 | -402 |
| 8 | Put Ratio Backspread (1x2) (#84) | 55.98 | +23280 | -416 |
| 9 | Synthetic Long Put (#147) | 51.64 | +23543 | -456 |
| 10 | Long LEAPS Put (#10) | 36.44 | +23358 | -641 |
| 11 | ZEBRA (Put) (#162) | 34.76 | +24106 | -693 |
| 12 | Long Put (Deep ITM) (#6) | 33.19 | +23977 | -722 |
| 13 | OTM Put Butterfly (Bearish Target) (#55) | 11.40 | +272 | -24 |
| 14 | Long Butterfly (Narrow) (#53) | 9.72 | +128 | -13 |
| 15 | Long Call Butterfly (#43) | 7.38 | +257 | -35 |
| 16 | Long Put Butterfly (#44) | 7.38 | +257 | -35 |
| 17 | Iron Butterfly (#46) | 6.99 | +255 | -36 |
| 18 | Portfolio Tail-Hedge Put Spread (#200) | 6.38 | +605 | -95 |
| 19 | OTM Call Butterfly (Bullish Target) (#54) | 6.15 | +248 | -40 |
| 20 | Batman (Double Butterfly) (#167) | 5.76 | +170 | -29 |
| 21 | Bearish Skewed Condor (#74) | 5.00 | +250 | -50 |
| 22 | Expiry-Day Pin Butterfly (#61) | 4.79 | +76 | -16 |
| 23 | Iron Butterfly (Wide Wings) (#56) | 3.98 | +393 | -99 |
| 24 | Put Condor (#67) | 3.76 | +237 | -63 |
| 25 | Iron Butterfly (Weekly) (#59) | 3.64 | +189 | -52 |


## Decision table E — credit (income) structures at a glance


The 77 option-only structures that open for a NET CREDIT (premium received up front — your edge is theta and an over-priced IV that decays):

> Short Call (Naked) (#7, credit 292); Short Put (Naked / Cash-Secured) (#8, credit 219); Bull Put Spread (Credit) (#17, credit 100); Bull Put Spread (Wide) (#18, credit 171); Bear Call Spread (Credit) (#19, credit 164); Bear Call Spread (Wide) (#20, credit 289); Bull Put Spread (Narrow / High Prob) (#23, credit 56); Bear Call Spread (Narrow / High Prob) (#24, credit 96); Deep-OTM Bear Call Spread (#26, credit 111); Short Straddle (#28, credit 774); Short Strangle (#30, credit 438); Short Strangle (Wide / 16-delta) (#32, credit 264); Short Guts (#34, credit 1107); Short Strangle (Weekly) (#38, credit 122); Short Straddle (45-DTE) (#40, credit 952); Short Strangle (10-delta) (#42, credit 181); Short Call Butterfly (#45, credit 35); Iron Butterfly (#46, credit 264); Broken-Wing Call Butterfly (#48, credit 53); Broken-Wing Put Butterfly (#49, credit 15); Skip-Strike Butterfly (Call) (#50, credit 160); Unbalanced (Ratio) Butterfly (#51, credit 129); Iron Butterfly (Wide Wings) (#56, credit 401); Broken-Wing Iron Butterfly (#57, credit 314); Put Broken-Wing (Income) (#58, credit 12); Iron Butterfly (Weekly) (#59, credit 198); Unbalanced Iron Butterfly (#62, credit 310); Iron Condor (#63, credit 174); Iron Condor (Wide) (#64, credit 167); Iron Condor (Narrow) (#65, credit 177); Broken-Wing Iron Condor (#69, credit 205); Unbalanced Iron Condor (#70, credit 238); Iron Condor (Weekly) (#71, credit 79); Iron Condor (10-delta) (#72, credit 98); Iron Condor (45-DTE) (#75, credit 229); Iron Condor (Credit-Skewed) (#78, credit 143); Call Ratio Spread (1x2) (#79, credit 128); Put Ratio Spread (1x2) (#80, credit 119); Call Ratio Spread (1x3) (#81, credit 282); Put Ratio Spread (1x3) (#82, credit 258); Call Ratio Spread (For Credit) (#87, credit 107); Put Ratio Spread (For Credit) (#88, credit 112); Front-Ratio Call Spread (#89, credit 115); Front-Ratio Put Spread (#90, credit 108); Put Ratio Spread (2x3) (#94, credit 20); Reverse Call Calendar (#103, credit 233); Reverse Put Calendar (#104, credit 96); Cash-Secured Put (Entry) (#116, credit 169); The Wheel (#117, credit 192); Short Put Ladder (Income) (#124, credit 366); Cash-Secured Put (Weekly) (#127, credit 83); Synthetic Short Stock (#144, credit 138); Jade Lizard (#155, credit 343); Reverse Jade Lizard (#156, credit 363); Big Lizard (#157, credit 482); Twisted Sister (#158, credit 555); Christmas Tree Butterfly (Call) (#159, credit 85); Christmas Tree Butterfly (Put) (#160, credit 43); Risk Reversal (Bearish) (#164, credit 73); Seagull (Bearish) (#166, credit 78); Iron Albatross (Ultra-Wide Condor) (#168, credit 166); Call Ratio Calendar (#171, credit 223); Put Ratio Calendar (#172, credit 222); Pterodactyl (Far-Wing Condor) (#174, credit 146); Bull Call Ladder (#175, credit 93); Bear Put Ladder (#176, credit 84); Double Iron Condor (#179, credit 234); Expiry-Day Short Straddle (#180, credit 140); Expiry-Day Iron Butterfly (#181, credit 102); Gap-Fade Bull Put Spread (#182, credit 52); High-IV Short Strangle (#184, credit 315); Post-Event IV-Crush Short Strangle (#187, credit 100); Budget-Day Iron Condor (#188, credit 22); Bank Nifty Intraday Short Straddle (#191, credit 140); Overnight Short Strangle (#192, credit 1); VIX-Spike Put Backspread (#193, credit 22); 45-DTE Theta-Harvest Condor (#195, credit 206).


## Decision table F — the situational playbook: what to trade when you see X

This is the table to internalise. Read the left column as *what you actually see on the screen or the calendar*, and the right column as your first-choice structures (turn to each numbered entry for the full plan). Always filter the suggestion through your own risk rule before trading.

| When you see... | First-choice structures |
|---|---|
| India VIX very low (~11-12), options look cheap | Low-IV Long Calendar (#185); Call Calendar (Horizontal) (#95); Long Straddle (Pre-Event) (#41); Call Ratio Backspread (1x2) (#83) |
| India VIX high (~20+), premium is rich and fear is in the tape | Iron Condor (#63); High-IV Short Strangle (#184); Jade Lizard (#155); Bull Put Spread (Credit) (#17) |
| IV rank above 70 (volatility expensive vs its own year) | Iron Butterfly (#46); Iron Condor (45-DTE) (#75); Short Strangle (10-delta) (#42); Bear Call Spread (Credit) (#19) |
| IV rank below 20 (volatility cheap, likely to expand) | Low-IV Long Calendar (#185); Double Calendar (#99); Long Strangle (#29); Put Ratio Backspread (1x2) (#84) |
| Strong uptrend with shallow pullbacks to support | Trend-Pullback Call Debit Spread (#183); Bull Call Spread (ATM) (#11); Poor Man's Covered Call (Diagonal) (#101); Stock-Replacement LEAPS (#197) |
| Strong downtrend, lower highs and lower lows | Bear Put Spread (ATM) (#14); Put Diagonal (#98); Bear Call Spread (Credit) (#19); Put Backspread (OTM) (#92) |
| Tight coiling range, low IV, a breakout looks imminent | Range-Breakout Long Strangle (#194); Reverse Iron Condor (#68); Long Straddle (#27) |
| Quiet, well-defined range you expect to hold | Iron Condor (#63); Long Call Butterfly (#43); Short Strangle (#30) |
| Expiry day and price is pinned near a round strike | Expiry-Day Iron Butterfly (#181); Expiry-Day Pin Butterfly (#61); Monthly-Expiry Butterfly (#190) |
| Union Budget day ahead (large fiscal-event tail) | Budget-Day Iron Condor (#188); Reverse Iron Butterfly (Event) (#60) |
| RBI policy decision in two days | RBI-Policy Calendar (#189); Low-IV Long Calendar (#185) |
| A single stock reports results tomorrow, IV is cheap | Earnings/Results Long Straddle (#186); Long Straddle (Pre-Event) (#41) |
| Just after results/an event — IV is about to crush | Post-Event IV-Crush Short Strangle (#187); Short Straddle (45-DTE) (#40) |
| Panicky gap-down on global news, you think it overshot | Gap-Fade Bull Put Spread (#182); Bull Put Spread (Narrow / High Prob) (#23) |
| You want to buy Nifty/a stock, but lower and get paid to wait | Cash-Secured Put (Entry) (#116); The Wheel (#117) |
| You are long and want regular income against the position | Covered Call (OTM) (#113); Covered Strangle (#118); Buy-Write (#125) |
| You are long and want cheap downside protection | Collar (#131); Costless (Zero-Cost) Collar (#132); Put-Spread Collar (#133) |
| You want a budgeted crash hedge for a whole portfolio | Portfolio Tail-Hedge Put Spread (#200); Tail-Risk Hedge (#138); Index Put Hedge Overlay (#142) |
| You expect an explosive move but not the direction | Long Straddle (#27); Reverse Iron Condor (#68); Long Strangle (#29) |
| You expect an explosive move UP specifically | Call Ratio Backspread (1x2) (#83); Slingshot (Call Backspread) (#169); Risk Reversal (Bullish) (#163) |
| You expect a slow grind up and want to be paid for it | Bull Put Spread (Credit) (#17); Call Ratio Spread (1x2) (#79); Jade Lizard (#155) |
| High IV you expect to collapse toward the mean | Short Straddle (45-DTE) (#40); Iron Butterfly (#46); Call Calendar (Horizontal) (#95) |
| Low IV you expect to expand ahead of a catalyst | Low-IV Long Calendar (#185); Long Straddle (#27); Call Ratio Backspread (1x2) (#83) |
| You are a beginner and want DEFINED risk only | Bull Call Spread (ATM) (#11); Iron Condor (#63); Long Call Butterfly (#43); Bear Put Spread (ATM) (#14) |
| The put skew is very steep (downside puts richly bid) | Put Ratio Spread (1x2) (#80); Jade Lizard (#155); Risk Reversal (Bullish) (#163) |
| Long-term bullish but want to free up capital | Stock-Replacement LEAPS (#197); Poor Man's Covered Call (Diagonal) (#101); Long LEAPS Call (#9) |
| Bank Nifty weekly, quiet open, you want fast theta (tiny size) | Bank Nifty Intraday Short Straddle (#191); Iron Butterfly (Weekly) (#59) |
| Mildly bullish within a range (a directional income lean) | Bullish Skewed Condor (#73); Broken-Wing Put Butterfly (#49); Bull Put Spread (Wide) (#18) |


## Decision table G — the core set every Nifty trader should master first

You do not need all 200 to be profitable. Master these dozen cold — what they are, when they win, how they lose — and you can handle almost any market the NSE throws at you. The other 188 are refinements of these core ideas.

| Core strategy | View | When it is the right tool |
|---|---|---|
| Long Call (ATM) (#1) | Strongly bullish | Convinced bullish, want leverage with capped risk and low IV. |
| Long Put (ATM) (#4) | Strongly bearish | Convinced bearish or buying portfolio insurance. |
| Bull Call Spread (ATM) (#11) | Moderately bullish | Moderately bullish; cheaper than a naked call. |
| Bear Put Spread (ATM) (#14) | Moderately bearish | Moderately bearish with defined risk. |
| Bull Put Spread (Credit) (#17) | Neutral to bullish | Neutral-to-bullish and IV is high — get paid to be patient. |
| Bear Call Spread (Credit) (#19) | Neutral to bearish | Neutral-to-bearish and IV is high. |
| Iron Condor (#63) | Range-bound, elevated IV | Range-bound with elevated IV — the workhorse income trade. |
| Iron Butterfly (#46) | Pin near ATM, high IV | Expect a pin near ATM with rich premium to sell. |
| Long Straddle (#27) | Big move, direction unknown | A big move is coming, direction unknown, and IV is cheap. |
| Covered Call (OTM) (#113) | Neutral to mildly bullish | You hold the underlying and want yield in a flat market. |
| Cash-Secured Put (Entry) (#116) | Bullish accumulation | You want to own lower and get paid while you wait. |
| Collar (#131) | Bullish, low-cost hedge | You are long and want near-free downside protection. |


## Decision table H — choosing the tenor (days to expiry)

Direction and volatility pick the family; the calendar picks the tenor. The same structure behaves very differently weekly versus monthly versus long-dated.

| Tenor | Character | Best-suited structures |
|---|---|---|
| **Weekly (0-7 DTE)** | Fast theta, vicious gamma — small size, active management | Expiry-day iron fly, weekly iron condor, pin butterfly, intraday short straddle (tiny) |
| **Monthly (20-45 DTE)** | The professional premium-selling window; manage at ~50% | 45-DTE iron condor, iron butterfly, short strangle, credit verticals, calendars |
| **Quarter / 60-90 DTE** | More vega, more room to be right; slower decay | Diagonals, double diagonals, protective collars, broken-wing flies |
| **LEAPS (180-365 DTE)** | Mostly delta and vega; theta is a slow bleed | Stock-replacement LEAPS, poor-man's covered call, long-dated protective puts |


## Decision table I — the Greeks signature of each family

Before you put on any structure, know its net Greeks: they tell you what actually moves your P&L. Delta is direction, theta is the daily drip of time, vega is your exposure to a change in implied volatility, gamma is how fast your delta itself moves.

| Family | Typical net delta | Theta | Vega | What dominates the P&L |
|---|---|---|---|---|
| Single long options | Directional (±) | Negative (hurts) | Positive (helps) | Direction + a vol move; time is the enemy |
| Debit verticals | Directional (±) | Mildly negative | Near zero | Direction; vega largely cancels |
| Credit verticals | Mild (±) | Positive (helps) | Negative | Theta + staying on the right side of the short strike |
| Long straddle/strangle | ~0 at entry | Negative (hurts) | Positive (helps) | Size of the move + rising IV |
| Short straddle/strangle | ~0 at entry | Positive (helps) | Negative | Time + falling IV; the tail is the danger |
| Butterflies (long) | ~0 near body | Positive near body | Negative | Pinning the body into expiry |
| Condors (iron) | ~0 in the zone | Positive (helps) | Negative | Price staying in the zone; theta harvest |
| Ratio spreads | Mild directional | Positive (helps) | Negative | Drift to the short strikes; the naked tail bites |
| Backspreads | Directional | Negative (hurts) | Positive (helps) | A big move plus rising IV |
| Calendars/diagonals | ~0 to mild | Positive (front decay) | Positive (helps) | Time decay of the front + rising IV |
| Covered/income | Long (+) | Positive (helps) | Negative | The underlying's direction, cushioned by premium |
| Protective/hedge | Long, floored | Negative (carry) | Positive (helps) | The underlying; the hedge caps the downside |


## Decision table J — the one thing that kills each family

Every structure has a single failure mode that does most of the damage. Know it before you enter.

| Family | The killer | The defence |
|---|---|---|
| Long options | Time decay while the move never comes (and IV crush after an event). | Buy when IV is low; give the trade time; size as a small bet. |
| Debit spreads | The move stalls short of the long strike. | Place strikes within a realistic move; take partial profits. |
| Credit spreads | A fast move blows through the short strike. | Size to the max loss; roll the untested side; stop at a multiple of the credit. |
| Short straddle/strangle | A gap or trend past the breakevens — uncapped loss. | Define the risk with wings; size tiny; hard stop at ~2x credit. |
| Butterflies | Price drifts away from the body. | Recentre by rolling; keep cost small; it is a low-probability bet. |
| Iron condors | A trend that runs out of the zone; gamma near expiry. | Manage at ~50% profit; exit by ~21 DTE; roll the tested side. |
| Ratio spreads | A strong move into the naked short strikes. | Always know where the tail is; add a wing; flatten the ratio. |
| Backspreads | Quiet, range-bound markets that bleed the debit. | Enter ahead of an expected catalyst; take the convex wing's profit. |
| Calendars | A big move away from the strike, or front IV that never rises. | Recentre; close into an IV spike; keep size modest. |
| Covered calls | A crash in the underlying (premium is a thin cushion). | Only on names you want to own; consider a collar in fear markets. |
| Cash-secured puts / wheel | A collapse in the underlying after assignment. | Sell on names you want; size to full assignment; roll down. |
| Hedges | Paying for protection that expires worthless, year after year. | Budget the cost; monetise puts after a fall; ratchet strikes up. |


## The ten laws of strategy selection

1. **View, then volatility, then the calendar.** Decide direction, then whether IV is cheap or rich, then the tenor. Never skip a step.

2. **Buy options when IV is low; sell premium when IV is high.** IV rank and India VIX are your fuel gauge — read them before you choose a side of volatility.

3. **Define your risk until you have earned the right not to.** Beginners trade only capped-loss structures. The uncapped column is for the experienced and the well-sized.

4. **Size to the max loss, not to the max profit.** No single trade should risk more than 1-2% of capital. The Max-loss column in this matrix is where position sizing starts.

5. **The high-probability trade has the small reward — and vice versa.** A 0.5 risk:reward credit spread wins often; a 5:1 butterfly wins rarely. Match the trade to your edge, not your hope.

6. **Manage winners early.** Most premium-selling structures are best closed at ~50% of max profit, well before expiry-week gamma turns on you.

7. **Have the exit before the entry.** Write down the profit target, the stop and the time-stop *before* you place the order. The scenario table in each entry is your map.

8. **Respect the event calendar.** Budget, RBI policy, results and expiry change which trade is right. The same structure is brilliant on Tuesday and reckless on expiry Thursday.

9. **One structure, one reason.** If you cannot say in a sentence why this trade and not a simpler one, trade the simpler one.

10. **Survival first.** The goal is to still be trading next year. Nine in ten retail F&O traders are not — and almost always because they ignored laws 3 and 4.


## How to use this matrix in practice

Trade from the map, not from a hunch. First fix your **view** (Table A) and your **volatility read** (Table B); the structures that appear in both lists are your candidates. Then apply your **risk rule** (Table C) — if you are still learning, stay out of the uncapped-loss column entirely and trade only defined-risk structures. Use Table D when you want a cheap, convex, low-probability bet and Table E when you want to be the seller of expensive premium. Finally, turn to the full entry (it carries the payoff diagram, the scenario P&L table and the management plan) and size the position so the Max-loss column is never more than 1–2% of your capital. That discipline — view, volatility, risk, size — is what separates the professional from the nine-in-ten who do not make it.
