"""Assemble the IN-DEPTH Illustrated Technical Analysis Handbook PDF.
Each topic: diagram + what it is + WHY it works + the market PSYCHOLOGY + how to trade it."""
import os
import re
import base64
import subprocess
import markdown
import fitz

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MD = os.path.join(ROOT, "interview_prep", "sources_md")  # markdown sources live here
IMG = os.path.join(HERE, "img")
PDF = os.path.join(ROOT, "interview_prep", "study_pdfs", "Technical_Research_Study_Guide.pdf")


def block(what, why, psych, trade, extra=None):
    s = (f"<b>What it is:</b> {what}<br>"
         f"<b>Why it works:</b> {why}<br>"
         f"<b>The psychology:</b> {psych}<br>"
         f"<b>How to use / trade it:</b> {trade}")
    if extra:
        s += f"<br><b>Interview depth:</b> {extra}"
    return s


def trade_plan_html(buy=None, stop=None, target=None):
    rows = ""
    if buy:
        rows += f"<br>&nbsp;&nbsp;&bull; <b>Buy / entry:</b> {buy}"
    if stop:
        rows += f"<br>&nbsp;&nbsp;&bull; <b>Stop-loss:</b> {stop}"
    if target:
        rows += f"<br>&nbsp;&nbsp;&bull; <b>Target / when to sell:</b> {target}"
    return (f'<br><span class="plan"><b>Trade plan — where to buy, stop and sell:</b>'
            f"{rows}</span>")


# Per-chart trade plan: image -> (buy/entry, stop-loss, target/when-to-sell)
TRADE_PLANS = {
    "02_patterns.png": (
        "After a bullish reversal candle (hammer / bullish engulfing) forms AT a support level, buy when "
        "the NEXT candle closes above the pattern's high (that confirms buyers followed through).",
        "Just below the pattern's low (under the wick) — if price goes there, the reversal failed.",
        "The next resistance level above, sized for at least 2:1 reward-to-risk. Sell there, or trail your "
        "stop up under each higher low."),
    "p2_double_bottom.png": (
        "Buy when price closes above the middle bounce high (the neckline).",
        "Just below the two bottoms.",
        "The pattern's height (bottoms-to-neckline) added to the breakout point."),
    "p2_double_top.png": (
        "Sell / exit longs when price closes below the middle low (the neckline).",
        "Just above the two tops.",
        "The pattern's height projected below the breakdown."),
    "p2_tri_ascending.png": (
        "Buy the close above the flat resistance top, ideally on a volume surge.",
        "Just inside the triangle.",
        "The triangle's height added to the breakout point."),
    "p2_tri_descending.png": (
        "Sell / short the close below the flat support bottom.",
        "Just inside the triangle.",
        "The triangle's height projected below the breakdown."),
    "p2_tri_symmetric.png": (
        "Trade the breakout in its direction (favour the prior trend), with volume.",
        "On the opposite side of the triangle.",
        "The triangle's widest (left-hand) height."),
    "p2_flag.png": (
        "Buy the breakout above the flag.",
        "Below the flag low.",
        "The flagpole height added to the breakout point."),
    "p2_cup.png": (
        "Buy the breakout above the handle's high.",
        "Below the handle.",
        "The cup's depth added to the breakout point."),
    "p5_call.png": (
        "Buy a call when your bullish setup triggers.",
        "Exit if the underlying breaks your stop, or cut at ~30-50% premium loss.",
        "Book profit at the underlying's target; don't ride it into expiry (theta decay)."),
    "p5_put.png": (
        "Buy a put when bearish, or to hedge a stock you own.",
        "Exit if the underlying reclaims your level.",
        "Book profit at the target; mind daily theta decay."),
    "p5_covered_call.png": (
        "Sell a call against stock you already own, in a sideways/mildly-bullish view.",
        "The real risk is the stock falling (premium gives a small cushion).",
        "Keep the premium if price stays below the strike; gains are capped above it."),
    "p5_straddle.png": (
        "Buy before a known event (results/budget) when a big move is expected.",
        "Time-based: exit if the move doesn't arrive, before the post-event IV crush.",
        "Take profit once the move exceeds the combined premium; exit quickly after the event."),
    "p5_bull_spread.png": (
        "Enter for a moderate bullish view (cheaper than a naked call).",
        "Max loss is fixed = the net premium paid.",
        "Max profit near the higher (sold) strike."),
    "p5_iron_condor.png": (
        "Enter when you expect a quiet, range-bound market.",
        "Act if price approaches one of your short strikes.",
        "Close at about 50% of max profit rather than holding to expiry."),
    "p2_star.png": (
        "Morning Star: buy when the 3rd (strong green) candle closes. Evening Star: sell/exit when the 3rd "
        "red candle closes.",
        "Just beyond the middle 'star' candle's extreme (below the low for a Morning Star).",
        "The prior swing high (Morning Star) or swing low (Evening Star); aim for 2:1 or better."),
    "04_support_resistance.png": (
        "Near SUPPORT, buy only once a bullish candle shows the level is holding (don't catch a falling "
        "knife). For a breakout, buy when a candle CLOSES above resistance — ideally on the retest from above.",
        "Just below support (or below the broken resistance on a breakout trade).",
        "The next resistance above. For a breakout, add the range's height to the breakout point. Sell into "
        "resistance or trail the stop."),
    "p2_trendlines.png": (
        "Buy when price bounces off the rising trendline and prints a bullish candle.",
        "Just below the trendline / the bounce low.",
        "The prior swing high; trail the stop up the line. EXIT if price closes decisively below the trendline."),
    "p2_headshoulders.png": (
        "This is a TOP pattern → SELL / exit longs (or short) when price closes below the neckline, or on a "
        "pullback that retests it. (Inverse H&amp;S: do the opposite — buy the upward neckline break.)",
        "Above the right shoulder.",
        "Project the head-to-neckline distance downward from the break — cover/target there."),
    "p2_doubletop.png": (
        "Double BOTTOM (W): buy on a close above the middle peak (neckline). Double TOP (M): sell on a close "
        "below the middle trough.",
        "Below the second low (bottom) / above the second high (top).",
        "Add the pattern's height to the breakout point."),
    "p2_triangles.png": (
        "Enter on the candle that CLOSES beyond the triangle line in the breakout direction — best with a "
        "volume surge. An ascending triangle favours upside breakouts.",
        "On the opposite side of the triangle (just inside the other trendline).",
        "Measure the triangle's tallest (left-hand) height and project it from the breakout point."),
    "p2_flag_cup.png": (
        "Buy the breakout above the flag's upper line / the cup's handle.",
        "Below the flag low / the handle low.",
        "Add the 'flagpole' height to the breakout point (a measured move)."),
    "p2_gaps.png": (
        "Breakaway gap (with volume): enter in the gap's direction on the open or first small pullback. "
        "Exhaustion gap: fade it — trade toward the gap getting filled.",
        "On the far side of the gap (a move back through it kills the idea).",
        "Trend continuation for a breakaway gap; the prior close (gap fill) for an exhaustion gap."),
    "05_moving_averages.png": (
        "In an uptrend, buy a pullback to the 20- or 50-day MA when a bullish candle forms on it. A golden "
        "cross (50 above 200) is a positional buy signal.",
        "Below the MA / the pullback low.",
        "The prior high; then trail with the MA and EXIT when price closes decisively below it."),
    "06_rsi.png": (
        "In a range, buy when RSI climbs back above 30 (out of oversold). Strongest when paired with bullish "
        "divergence AND a break of short-term price structure.",
        "Below the recent swing low (or the divergence low).",
        "Sell when RSI reaches ~70 (overbought) in a range, or at the next resistance. Do NOT blindly short "
        "RSI &gt; 70 in a strong uptrend."),
    "07_macd.png": (
        "Go long on a bullish crossover (MACD line crosses above the signal line), ideally above the zero line.",
        "Below the recent swing low.",
        "Sell/exit on the bearish crossover (MACD back below signal), or at the next resistance. A shrinking "
        "histogram = tighten your stop."),
    "p3_stochastic.png": (
        "In a range, buy when %K crosses above %D while below the 20 line (oversold).",
        "Below the recent swing low.",
        "Sell when stochastic crosses down from above the 80 line (overbought)."),
    "08_bollinger.png": (
        "Range play: buy at the LOWER band when a bullish candle prints. Squeeze play: buy on a close OUTSIDE "
        "the upper band after the bands have pinched tight.",
        "Range: below the lower band. Breakout: back at the middle band (20-MA).",
        "Range: the middle or upper band. Breakout: ride until price closes back inside the bands."),
    "p3_atr.png": (
        "ATR is not an entry trigger — it SIZES your risk on whatever setup you take.",
        "Place the stop about 1.5–2× ATR away from entry, so normal daily noise won't knock you out.",
        "Set the target in ATR multiples too (e.g. 3× ATR) so reward-to-risk stays 2:1 or better."),
    "p3_volume.png": (
        "Only trust a breakout entry when volume EXPANDS on the breakout candle.",
        "Standard (below the broken level).",
        "Standard target — but exit early if the move is running on fading volume (no conviction)."),
    "09_fibonacci.png": (
        "In an uptrend, place buy orders in the 38.2%–61.8% retracement zone; enter on a bullish candle there "
        "(strongest where a Fib level overlaps support or a moving average).",
        "Just below the 61.8% level (or the swing low) — beyond it the trend is in doubt.",
        "The prior high (0% level); then Fibonacci EXTENSIONS at 1.272× and 1.618× for runners."),
    "p3_pivots.png": (
        "Intraday with an up-bias: buy near the central Pivot or S1 when it holds.",
        "Below the next pivot level down.",
        "R1 first, then R2; sell / scale out at the resistance pivots."),
    "p4_divergence.png": (
        "Don't buy on divergence alone — wait for price to BREAK its short-term trendline / structure, then enter.",
        "Beyond the divergence extreme (the price high or low that created it).",
        "The prior support/resistance; divergence reversals can run far, so trail the stop."),
    "03_trend.png": (
        "Buy dips toward the higher lows in an uptrend; sell rallies into lower highs in a downtrend.",
        "Below the most recent higher low (in an uptrend).",
        "The next higher high; trail to ride the trend. EXIT when structure breaks (first lower low)."),
    "p4_elliott.png": (
        "The best entry is the start of wave 3 (right after the wave-2 pullback) — the longest, strongest wave.",
        "Below the wave-2 low.",
        "Wave 3 often extends to 1.618× wave 1; take profit / tighten in wave 5 (exhaustion)."),
    "p5_call_put.png": (
        "Buy a CALL when your bullish setup triggers (breakout or support holds); buy a PUT when bearish.",
        "Exit the option if the underlying breaks your stop level, or cut at roughly a 30–50% premium loss.",
        "Book profit when the underlying hits your target; don't ride it into expiry where theta decay eats you."),
    "p5_income_straddle.png": (
        "Buy a straddle/strangle BEFORE a known event (results, budget) when a big move is expected but "
        "direction is unknown.",
        "Time-based: exit if the expected move doesn't arrive, before theta and the post-event IV crush erode it.",
        "Take profit once the move exceeds the combined premium; exit quickly after the event (IV collapses fast)."),
    "p5_spreads.png": (
        "Bull call spread for a moderate bullish view (cheaper than a naked call); iron condor when you expect "
        "a quiet, range-bound market.",
        "Max loss is defined by the structure; on a condor, act if price approaches your short strike.",
        "Spread: toward the short strike. Condor: close at about 50% of max profit rather than holding to expiry."),
    "p5_oi_chain.png": (
        "Treat the highest-PUT-OI strike as support (buy bounces near it) and the highest-CALL-OI strike as "
        "resistance (sell/short into it).",
        "Just beyond the OI 'wall' you are trading against.",
        "The opposite OI wall; near expiry price often gravitates toward the max-pain strike."),
    "p5_iv_skew.png": (
        "BUY options (calls/puts) when IV is LOW (they're cheap); SELL premium (spreads/condors) when IV is HIGH.",
        "Manage by the underlying's price level, as in any trade.",
        "For long options, exit BEFORE an expected IV crush (e.g. right after a results announcement)."),
    "p6_gold_dollar.png": (
        "Lean LONG gold when the dollar / real yields are falling or fear is rising; lean SHORT when the "
        "dollar strengthens.",
        "Below gold's nearest support level.",
        "The next resistance — confirm with the usual technicals (trend, RSI, levels)."),
    "p7_vix.png": (
        "A VIX spike to an extreme near a major support level = look to BUY the index (fear is peaking).",
        "Below that support level.",
        "A mean-reversion bounce; trim the position as VIX falls back toward normal."),
    "p8_riskreward.png": (
        "Only take the trade if, from your entry, the distance to a sensible target is at least 2× the "
        "distance to your stop.",
        "At the price that proves your idea WRONG (below support/structure) — never an arbitrary percentage.",
        "At least 2× your risk; scale out part at 1× and trail the rest."),
    "10_setup.png": (
        "Uptrend confirmed + pullback to support/MA + a bullish trigger candle → buy.",
        "Just below that support / moving average.",
        "The next resistance or a measured move, sized for 2:1+; trail the stop to ride the trend."),
}


def deep(parts, formula=None, example=None):
    s = f"<b>Every part, explained simply:</b> {parts}"
    if formula:
        s += f"<br><b>How it's calculated (formula):</b> {formula}"
    if example:
        s += f"<br><b>Worked example:</b> {example}"
    return s


# Beginner deep-dive per chart: define every component + (for indicators) formula + worked example
DEEP = {
    "01_anatomy.png": deep(
        "One candle = one day (or week/month). It packs four prices: <b>Open</b> (first price), "
        "<b>Close</b> (last price), <b>High</b> (highest), <b>Low</b> (lowest). The thick <b>body</b> runs "
        "from open to close; if the close is higher than the open it's <b>green</b> (buyers won), else "
        "<b>red</b> (sellers won). The thin <b>wicks</b> show the high and low — a long wick means price "
        "went there but was pushed back."),
    "p2_patterns.png": deep(
        "Four classic reversal candles:<br>"
        "&nbsp;&nbsp;&bull; <b>Doji</b> &mdash; open and close almost equal (tiny body) = buyers and "
        "sellers balanced = indecision, often before a turn.<br>"
        "&nbsp;&nbsp;&bull; <b>Hammer</b> &mdash; small body on top, long lower wick; after a fall it shows "
        "buyers slammed price back up = bullish.<br>"
        "&nbsp;&nbsp;&bull; <b>Bullish Engulfing</b> &mdash; a big green candle completely covers the "
        "previous red one = buyers overwhelmed sellers = strong reversal up.<br>"
        "&nbsp;&nbsp;&bull; <b>Shooting Star</b> &mdash; small body at the bottom, long upper wick; after a "
        "rise it shows sellers rejected higher prices = bearish.<br>"
        "They matter most AT a support/resistance level, on above-average volume."),
    "02_patterns.png": deep(
        "A <b>hammer</b> has a small body at the top and a long lower wick. The story: sellers shoved price "
        "far down during the day (long tail), but buyers fought it all the way back up by the close — so "
        "buyers are taking over. You don't buy the hammer itself; you wait for the NEXT candle to close "
        "higher, which confirms the reversal. Strongest when it appears right at a support level."),
    "03_trend.png": deep(
        "Ignore the small wiggles and look at the staircase. <b>Uptrend</b> = each high is higher than the "
        "last (higher highs) and each dip stops higher than the last (higher lows). <b>Downtrend</b> = "
        "lower highs and lower lows. <b>Sideways</b> = a flat range. The trend 'breaks' the first time the "
        "staircase fails — e.g., in an uptrend, the first LOWER low."),
    "04_support_resistance.png": deep(
        "<b>Support</b> is a price floor where buyers keep stepping in and stop the fall. <b>Resistance</b> "
        "is a ceiling where sellers keep appearing and stop the rise. They exist because markets have "
        "memory — traders remember those levels and act there again. When price finally breaks through a "
        "ceiling, that old resistance often becomes the new support (doubters now buy the dip back to it)."),
    "p2_trendlines.png": deep(
        "A trendline is a straight line drawn under the rising lows of an uptrend (or over the falling "
        "highs of a downtrend). It's a sloping version of support: each time price dips to the line, buyers "
        "step in. You need two touches to draw it and a third to trust it. A clean break of the line is an "
        "early warning the trend is changing."),
    "05_moving_averages.png": deep(
        "A moving average is the average of the last N closing prices, recalculated each day so it 'moves'. "
        "A <b>fast</b> MA (e.g. 20-day) hugs price and reacts quickly; a <b>slow</b> MA (50- or 200-day) "
        "shows the big trend. <b>SMA</b> weights every day equally; <b>EMA</b> weights recent days more so "
        "it turns faster.",
        "<code>SMA = (P1 + P2 + ... + PN) / N</code>. EMA: <code>EMA = Price&times;k + EMA_prev&times;(1&minus;k)</code>, "
        "where <code>k = 2/(N+1)</code>.",
        "Last 5 closes 10, 12, 14, 16, 18 &rarr; SMA(5) = 70 &divide; 5 = <b>14</b>. For a 10-day EMA, "
        "k = 2/11 = 0.18; if yesterday's EMA was 100 and today's price 110 &rarr; 110&times;0.18 + 100&times;0.82 = <b>101.8</b>."),
    "06_rsi.png": deep(
        "RSI is one line travelling 0&ndash;100 in its own panel. It measures momentum: how big the up-days "
        "have been versus the down-days over the last 14 days. <b>Above 70</b> = overbought (risen too "
        "fast), <b>below 30</b> = oversold (fallen too fast), <b>50</b> = balance between buyers and sellers.",
        "<code>RS = Average Gain &divide; Average Loss</code> (over 14 days), then "
        "<code>RSI = 100 &minus; 100/(1 + RS)</code>.",
        "If the average gain is 1.0 and average loss 0.5 &rarr; RS = 2 &rarr; RSI = 100 &minus; 100/3 = "
        "<b>66.7</b>. Sanity check: all up-days &rarr; RSI 100; all down-days &rarr; RSI 0; equal &rarr; 50."),
    "06b_rsi_divergence.png": deep(
        "Divergence = price and the RSI line disagree. To spot it, follow the red dots on the chart:<br>"
        "&nbsp;&nbsp;&bull; <b>Step 1:</b> mark the last two major <b>highs</b> on the PRICE chart (top).<br>"
        "&nbsp;&nbsp;&bull; <b>Step 2:</b> mark the matching two highs on the RSI line (bottom).<br>"
        "&nbsp;&nbsp;&bull; <b>Step 3:</b> compare them &mdash;<br>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&ndash; Price <b>Higher High</b> + RSI <b>Lower High</b> &rarr; <b>Bearish "
        "divergence</b> (rally weakening &rarr; expect a fall).<br>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&ndash; Price <b>Lower Low</b> + RSI <b>Higher Low</b> &rarr; <b>Bullish "
        "divergence</b> (fall weakening &rarr; expect a bounce).<br>"
        "Why it matters: price made a new high, but RSI shows the momentum behind it was actually weaker "
        "&mdash; fewer, tired buyers. An early warning the trend may reverse."),
    "07_macd.png": deep(
        "MACD has THREE parts:<br>"
        "&nbsp;&nbsp;&bull; <b>MACD line</b> (main line) = a fast 12-day EMA minus a slow 26-day EMA &mdash; "
        "it measures how far the short-term average has pulled away from the long-term one.<br>"
        "&nbsp;&nbsp;&bull; <b>Signal line</b> = a 9-day EMA OF the MACD line &mdash; a smoothed, slower copy "
        "used as the trigger.<br>"
        "&nbsp;&nbsp;&bull; <b>Histogram</b> (the bars) = the MACD line minus the Signal line. Tall bars = "
        "lines far apart = strong momentum; shrinking bars = lines converging = momentum fading. Bars flip "
        "above zero exactly when the MACD line crosses above the signal line.",
        "<code>MACD = EMA(12) &minus; EMA(26)</code>; <code>Signal = EMA(9) of MACD</code>; "
        "<code>Histogram = MACD &minus; Signal</code>.",
        "If the 12-EMA = 1020 and 26-EMA = 1000 &rarr; MACD = +20. If the signal line = 15 &rarr; "
        "histogram = +5 (positive = bullish; the MACD line is above its signal)."),
    "p3_stochastic.png": deep(
        "Two lines, 0&ndash;100: <b>%K</b> answers 'where did price close inside its recent range?' "
        "(0 = at the very low, 100 = at the very high). <b>%D</b> is a 3-day average of %K &mdash; the "
        "smoother trigger line. Above 80 = closing near the highs (overbought); below 20 = near the lows "
        "(oversold).",
        "<code>%K = (Close &minus; Lowest Low) &divide; (Highest High &minus; Lowest Low) &times; 100</code> "
        "(over 14 days); <code>%D = 3-day average of %K</code>.",
        "If over 14 days the low was 40, the high 60 and today's close 58 &rarr; %K = (58&minus;40)/(60&minus;40)"
        "&times;100 = <b>90</b> (closed near the top = strong)."),
    "p3_adx.png": deep(
        "ADX comes with TWO companion lines that show DIRECTION:<br>"
        "&nbsp;&nbsp;&bull; <b>+DI line (green)</b> = the strength of UPWARD (bullish) price movement.<br>"
        "&nbsp;&nbsp;&bull; <b>&minus;DI line (red)</b> = the strength of DOWNWARD (bearish) price movement.<br>"
        "When +DI (green) is above &minus;DI (red), buyers are in control; when &minus;DI is on top, sellers "
        "are. The <b>ADX line</b> itself (0&ndash;100) measures only how STRONG the trend is, not its "
        "direction: above 25 = strong trend, below 20 = weak/sideways.",
        "<code>+DI = 100 &times; smoothed(+DM) &divide; ATR</code>; <code>&minus;DI = 100 &times; "
        "smoothed(&minus;DM) &divide; ATR</code>; <code>DX = 100 &times; |+DI &minus; &minus;DI| &divide; "
        "(+DI + &minus;DI)</code>; <code>ADX = smoothed average of DX</code>.",
        "If +DI = 30 and &minus;DI = 10 &rarr; DX = 100 &times; |30&minus;10| &divide; (30+10) = 100 &times; "
        "20/40 = <b>50</b> &mdash; a strong uptrend (buyers clearly dominating)."),
    "08_bollinger.png": deep(
        "Developed by John Bollinger in the 1980s to measure volatility and flag overbought/oversold "
        "conditions. THREE lines wrap around price:<br>"
        "&nbsp;&nbsp;&bull; <b>Middle band</b> = a 20-day Simple Moving Average &mdash; the baseline for the "
        "intermediate trend.<br>"
        "&nbsp;&nbsp;&bull; <b>Upper band</b> = middle + 2 standard deviations &mdash; touching it signals "
        "potential <b>overbought</b> territory.<br>"
        "&nbsp;&nbsp;&bull; <b>Lower band</b> = middle &minus; 2 standard deviations &mdash; touching it "
        "signals potential <b>oversold</b> territory.<br>"
        "<b>Standard deviation (&sigma;)</b> measures how far prices stray from their average &mdash; i.e. "
        "volatility.<br>"
        "<b>Three core ideas:</b> (1) <b>Volatility &mdash; squeeze &amp; bulge:</b> the bands widen when "
        "volatility is high and tighten when it's low; a tight <b>squeeze</b> warns of an explosive breakout "
        "coming. (2) <b>Mean reversion &mdash; the bounce:</b> ~95% of price action stays inside the bands, "
        "so a tag of the upper/lower band often snaps back toward the middle. (3) <b>Trend confirmation &mdash; "
        "walking the band:</b> in a strong trend price can 'ride' the upper (or lower) band instead of "
        "reversing &mdash; so don't blindly fade a band touch in a powerful trend. Best used WITH a momentum "
        "tool like RSI or MACD to avoid false signals.",
        "<code>Middle = SMA(20)</code>; <code>Upper = Middle + 2&sigma;</code>; "
        "<code>Lower = Middle &minus; 2&sigma;</code> (&sigma; = standard deviation of the last 20 closes).",
        "If the 20-day average = 100 and &sigma; = 5 &rarr; Upper = 100 + 10 = <b>110</b>, "
        "Lower = 100 &minus; 10 = <b>90</b>. About 95% of prices stay between the bands."),
    "p3_atr.png": deep(
        "ATR tells you how much an asset typically moves in ONE day, in points/rupees &mdash; a pure "
        "volatility number with no direction. It uses the 'True Range', the biggest of three measures so it "
        "also captures overnight gaps.",
        "<code>True Range = the largest of: (High &minus; Low), |High &minus; PrevClose|, "
        "|Low &minus; PrevClose|</code>; <code>ATR = 14-day average of True Range</code>.",
        "Today's High = 105, Low = 100, yesterday's Close = 102 &rarr; TR = max(5, |105&minus;102|=3, "
        "|100&minus;102|=2) = <b>5</b>. Average 14 of these for the ATR."),
    "p3_volume.png": deep(
        "Volume is simply the number of shares/contracts traded each day, drawn as bars under price. No "
        "formula &mdash; you compare bar heights. A tall bar = many participants (high conviction); a short "
        "bar = few (weak conviction).",
        None,
        "A breakout candle with a volume bar 2&ndash;3&times; the recent average = trustworthy. The same "
        "breakout on a below-average bar = likely a fake-out."),
    "09_fibonacci.png": deep(
        "You draw the Fib tool from a recent swing LOW to a recent swing HIGH and it auto-plots horizontal "
        "lines at 23.6%, 38.2%, 50% and 61.8% of that move &mdash; the levels where a pullback tends to "
        "pause. The numbers come from the Fibonacci sequence (1,1,2,3,5,8,13&hellip;); dividing neighbours "
        "gives ~61.8%.",
        "<code>Level = High &minus; (percentage &times; (High &minus; Low))</code>.",
        "Move from Low 100 to High 200 (range 100): 38.2% level = 200 &minus; 0.382&times;100 = <b>161.8</b>; "
        "61.8% level = 200 &minus; 0.618&times;100 = <b>138.2</b>. Buyers often re-enter in the 138&ndash;162 zone."),
    "p3_pivots.png": deep(
        "Pivot points are the day's support/resistance levels, computed from YESTERDAY's high, low and "
        "close. The central <b>Pivot (P)</b> is the day's 'fair value'; <b>R1, R2</b> are resistances above; "
        "<b>S1, S2</b> are supports below.",
        "<code>P = (High + Low + Close) &divide; 3</code>; <code>R1 = 2P &minus; Low</code>; "
        "<code>S1 = 2P &minus; High</code>; <code>R2 = P + (High &minus; Low)</code>; "
        "<code>S2 = P &minus; (High &minus; Low)</code>.",
        "Yesterday H = 110, L = 100, C = 105 &rarr; P = 105, R1 = 2&times;105&minus;100 = <b>110</b>, "
        "S1 = 2&times;105&minus;110 = <b>100</b>, R2 = 115, S2 = 95."),
    "p4_divergence.png": deep(
        "Same idea as RSI divergence but it applies to any momentum indicator (RSI or MACD). Compare the "
        "indicator's peaks/troughs to price's: if price makes a new extreme that the indicator does NOT "
        "match, the move is losing power. <b>Regular</b> divergence warns of a reversal; <b>hidden</b> "
        "divergence (price higher low, indicator lower low in an uptrend) signals the trend will continue."),
    "p4_elliott.png": deep(
        "Developed by Ralph Nelson Elliott (1930s): prices move in repeating <b>8-wave cycles (a 5-3 "
        "structure)</b> driven by crowd psychology.<br>"
        "<b>The 5-wave Motive (Impulse) phase</b> &mdash; moves WITH the main trend:<br>"
        "&nbsp;&nbsp;&bull; <b>Wave 1</b> &mdash; first move up, a few early buyers.<br>"
        "&nbsp;&nbsp;&bull; <b>Wave 2</b> &mdash; pullback as early buyers take profit, but it does NOT fall "
        "below the start of Wave 1.<br>"
        "&nbsp;&nbsp;&bull; <b>Wave 3</b> &mdash; usually the longest, strongest wave; good news pulls the "
        "public in and price surges.<br>"
        "&nbsp;&nbsp;&bull; <b>Wave 4</b> &mdash; a mild profit-taking dip that does NOT enter Wave 1's price "
        "territory.<br>"
        "&nbsp;&nbsp;&bull; <b>Wave 5</b> &mdash; the final push; optimism is extreme and the asset is often "
        "overvalued (watch for divergence here).<br>"
        "<b>The 3-wave Corrective phase</b> &mdash; moves AGAINST the trend (a breather), labelled A-B-C:<br>"
        "&nbsp;&nbsp;&bull; <b>Wave A</b> &mdash; first move against the trend; many mistake it for a normal dip.<br>"
        "&nbsp;&nbsp;&bull; <b>Wave B</b> &mdash; a bounce that fools people into thinking the old trend is back.<br>"
        "&nbsp;&nbsp;&bull; <b>Wave C</b> &mdash; a sharp drop that confirms the correction.<br>"
        "<b>Core ideas:</b> waves are <b>fractal</b> (zoom in and a small 8-wave cycle sits inside a bigger "
        "wave, like nested Russian dolls); practitioners use <b>Fibonacci ratios</b> (38.2%, 50%, 61.8%) to "
        "estimate how deep corrections go and how far impulse waves run.<br>"
        "<b>Three rules that MUST hold for a valid count:</b> (1) Wave 2 never retraces more than 100% of "
        "Wave 1; (2) Wave 3 is never the shortest of waves 1, 3 and 5; (3) Wave 4 never overlaps Wave 1's "
        "price territory.<br>"
        "Because counting waves is subjective, always confirm with other tools (moving averages, momentum "
        "oscillators)."),
    "p2_headshoulders.png": deep(
        "Picture a silhouette: left shoulder, higher head, right shoulder. The market rallies (left "
        "shoulder), pulls back, rallies to a NEW high (head), pulls back, then only reaches a LOWER high "
        "(right shoulder) &mdash; buyers are weakening. The <b>neckline</b> is the support under the two "
        "pullback lows; a break below it starts the fall. Target &asymp; the height from head to neckline."),
    "p2_doubletop.png": deep(
        "<b>Double Bottom (W)</b>: price falls to a level, bounces, falls to the SAME level, bounces again "
        "&mdash; that level refused to break twice = strong support = reversal up. Buy when price breaks "
        "above the middle bounce high (the neckline). <b>Double Top (M)</b> is the mirror: two failed pushes "
        "at the same ceiling = reversal down."),
    "p2_triangles.png": deep(
        "A triangle is price squeezing into a tighter range &mdash; a standoff that must break. "
        "<b>Ascending</b> (flat top, rising bottoms) = buyers getting aggressive &rarr; usually breaks UP. "
        "<b>Descending</b> (flat bottom, falling tops) &rarr; usually breaks DOWN. <b>Symmetrical</b> (both "
        "squeezing) &rarr; breaks in the direction of the existing trend. Trade the breakout candle, ideally "
        "with a volume surge."),
    "p2_flag_cup.png": deep(
        "<b>Bull flag</b>: after a sharp rally (the flagpole), price drifts sideways/slightly down in a "
        "small rectangle (the flag) as early buyers take profit; once weak hands are out, the trend "
        "resumes &mdash; buy the breakout above the flag. <b>Cup &amp; handle</b>: price carves a rounded U "
        "(the cup), then a small dip (the handle), then breaks out up."),
    "p2_gaps.png": deep(
        "A gap is a blank space where price jumps overnight (opens far from the prior close), usually on "
        "big news. A <b>breakaway gap</b> with heavy volume often starts a strong new trend (trade with "
        "it). An <b>exhaustion gap</b> at the end of a long move (last euphoric/panicked traders) often "
        "reverses. Gaps frequently get 'filled' as price drifts back to where the jump began."),
    "p2_star.png": deep(
        "Both are three-candle reversals. <b>Morning Star</b> (bullish): a big down candle, then a small "
        "'star' candle (indecision = the dominant sellers lose steam), then a big up candle = bottom. "
        "<b>Evening Star</b> (bearish): big up candle, small star, big down candle = top. The little middle "
        "candle is the moment the crowd's belief cracks."),
    "p1_cycle.png": deep(
        "Every trend has four phases. <b>Accumulation</b>: smart money quietly buys at the bottom while the "
        "public is fearful (sideways, low volume). <b>Mark-up</b>: the public notices and piles in &mdash; "
        "the biggest rally. <b>Distribution</b>: smart money quietly sells to the greedy crowd at the top. "
        "<b>Mark-down</b>: the decline. Knowing the phase tells you whether to buy or be cautious."),
    "p1_timeframes.png": deep(
        "Always read two timeframes. The <b>higher</b> one (e.g. weekly) shows the dominant trend &mdash; "
        "your context and bias. The <b>lower</b> one (e.g. daily/hourly) is where you time the entry. Rule: "
        "only trade in the direction of the higher timeframe; if they conflict, it's a low-conviction trade."),
    "p1_charttypes.png": deep(
        "Same prices, three views. <b>Line</b> connects only the closes &mdash; cleanest for spotting the "
        "big trend. <b>Bar (OHLC)</b> shows open-high-low-close as a tick chart. <b>Candlestick</b> shows "
        "the same four prices but colour-coded so you instantly see who won the day &mdash; the global "
        "standard."),
    "p5_futures_curve.png": deep(
        "<b>Spot price</b> = the price if you buy TODAY (immediate delivery). <b>Futures price</b> = a price "
        "you fix today to buy/sell on a future date (a futures contract).<br>"
        "<b>Contango (the normal market):</b> the futures price is HIGHER than spot. Why? Holding an asset "
        "until later has costs &mdash; interest on money, storage, insurance &mdash; together called the "
        "<b>cost of carry</b>. The futures curve slopes UP. Memory: <b>Future &gt; Spot = Contango</b>.<br>"
        "<b>Backwardation (unusual):</b> the futures price is LOWER than spot. This happens with strong "
        "IMMEDIATE demand or a shortage &mdash; everyone wants the asset NOW, so today's price is bid up "
        "above the future. The curve slopes DOWN. Memory: <b>Spot &gt; Future = Backwardation</b> (think of "
        "one bottle of water in a desert: huge demand today, but rain may come in 3 months).<br>"
        "<b>Where you see backwardation:</b> mostly commodities &mdash; crude oil, natural gas, wheat, "
        "sometimes gold &mdash; because real shortages happen.<br>"
        "<b>Trading meaning:</b> contango = normal, nothing special; backwardation = strong current demand / "
        "tight supply, often a bullish or shortage signal.<br>"
        "<b>30-second interview answer:</b> 'Contango is when the futures price is above spot, usually due to "
        "the cost of carry (interest, storage, insurance) &mdash; the normal state. Backwardation is the "
        "opposite, futures below spot, typically from strong immediate demand or a shortage. The "
        "relationship between spot and futures prices across expiries is the futures curve.'",
        "<code>Futures Price = Spot Price + Cost of Carry</code> (cost of carry = interest + storage + "
        "insurance &minus; any income such as dividends).",
        "Spot &#8377;100, interest &#8377;2, storage &#8377;1, insurance &#8377;1 &rarr; Future = "
        "100+2+1+1 = <b>&#8377;104</b> (contango). But if crude turns suddenly scarce and everyone needs it "
        "now: Spot &#8377;100, 3-month Future &#8377;97 &rarr; Future &lt; Spot = <b>backwardation</b>."),
    "p5_call_put.png": deep(
        "Key words: <b>Strike</b> = the fixed price in the contract. <b>Premium</b> = what you pay to buy "
        "the option (your max loss as a buyer). <b>Expiry</b> = the deadline. A <b>Call</b> profits if price "
        "rises above the strike; a <b>Put</b> profits if price falls below it.",
        "<code>Call profit at expiry = max(Spot &minus; Strike, 0) &minus; Premium</code>; "
        "<code>Breakeven = Strike + Premium</code>.",
        "Buy a 24,000 Call for &#8377;100. If Nifty expires at 24,250 &rarr; value = 24,250 &minus; 24,000 = "
        "250; profit = 250 &minus; 100 = <b>&#8377;150</b>. Breakeven was 24,100."),
    "p5_oi_chain.png": deep(
        "<b>Open Interest (OI)</b> = the number of option contracts still open at each strike. Big OI = a "
        "lot of money parked there. The strike with the highest <b>call</b> OI acts as resistance (call "
        "sellers defend it); the highest <b>put</b> OI acts as support. <b>PCR</b> (put-call ratio) = total "
        "put OI &divide; call OI &mdash; a sentiment gauge; very high PCR can be contrarian bullish."),
    "p5_iv_skew.png": deep(
        "<b>Implied Volatility (IV)</b> = the market's expectation of future movement, baked into option "
        "prices &mdash; high IV = expensive options (big moves expected), low IV = cheap (calm expected). "
        "The <b>skew</b> means IV differs by strike: downside puts usually cost more because investors fear "
        "crashes and pay up for protection. There's no neat formula &mdash; IV is solved by reversing the "
        "Black-Scholes pricing model."),
    "p8_riskreward.png": deep(
        "Three prices define every trade: <b>Entry</b> (where you buy), <b>Stop-loss</b> (exit if wrong), "
        "<b>Target</b> (take profit). Reward = entry-to-target distance; Risk = entry-to-stop distance.",
        "<code>Reward : Risk = (Target &minus; Entry) &divide; (Entry &minus; Stop)</code>.",
        "Buy at 100, target 112, stop 96 &rarr; reward = 12, risk = 4 &rarr; ratio = <b>3 : 1</b>. At 3:1 "
        "you can be wrong on 2 of every 3 trades and still break even."),
    "p8_drawdown.png": deep(
        "Drawdown is how far your account has fallen from its highest point (peak). Max drawdown = the "
        "worst such fall &mdash; the most pain you'd have had to sit through.",
        "<code>Drawdown = (Peak &minus; Trough) &divide; Peak</code>.",
        "If equity went 100 &rarr; 150 &rarr; 90, the peak was 150 and trough 90 &rarr; "
        "drawdown = (150&minus;90)/150 = <b>40%</b>."),
}


PARTS = [
    ("PART 1 — Foundations", [
        ("p1_charttypes.png", "Three ways to draw price", block(
            "The same price history shown as a line (closes only), a bar (OHLC), or a candlestick chart.",
            "Candlesticks encode four prices (open, high, low, close) plus the winner of the day in one "
            "visual symbol, so you read the balance of power at a glance — that's why they became the global standard.",
            "Each candle is a snapshot of a battle between buyers and sellers. A big body = one side dominated; "
            "small body or long wicks = conflict and indecision. Charts work because they are a picture of "
            "collective human emotion, and emotion repeats.",
            "Use candlesticks as your default; drop to a line chart when you just want to see the clean trend "
            "without noise.")),
        ("01_anatomy.png", "What one candle tells you", block(
            "Body = open-to-close range; wicks/shadows = the high and low; green = closed up, red = closed down.",
            "The body shows who won and by how much; the wicks show where price was rejected. A long upper wick "
            "means buyers pushed up but sellers slammed it back (supply); a long lower wick means sellers pushed "
            "down but buyers absorbed it (demand).",
            "A long body reflects conviction — one side overpowered the other all session. A tiny body reflects "
            "a stalemate. Wicks are 'rejection': the market visited a price and refused to stay there, which tells "
            "you where strong orders sit.",
            "Read the wick direction for hidden supply/demand: repeated long lower wicks at a level = buyers "
            "defending it (likely support).")),
        ("p1_cycle.png", "The market cycle (Dow / Wyckoff)", block(
            "Every trend moves through four phases: Accumulation, Mark-up, Distribution, Mark-down.",
            "Markets are driven by 'smart money' (institutions) who must buy and sell in size without moving "
            "price against themselves — so they accumulate quietly at bottoms and distribute quietly at tops, "
            "creating the repeating cycle.",
            "Accumulation happens during maximum pessimism (everyone has given up selling). Mark-up is when the "
            "public notices and FOMO drives the biggest rally. Distribution is peak euphoria, where smart money "
            "sells to the late, greedy crowd. Mark-down is the painful unwinding. It's fear → greed → fear.",
            "Identify the phase from price+volume: sideways ranges after a big fall (low volume) often = "
            "accumulation; sideways after a big rally with high churn = distribution.",
            "This is the backbone of Dow Theory and Wyckoff — name it and explain that smart money buys when "
            "retail panics and sells when retail is euphoric.")),
        ("p1_timeframes.png", "Multiple-timeframe analysis", block(
            "Reading the same asset on a higher timeframe (weekly) and a lower one (daily) together.",
            "A signal aligned with the bigger trend has the wind at its back; a signal against it is fighting "
            "a stronger force and usually fails.",
            "Different participants act on different timeframes — long-term investors set the tide, short-term "
            "traders create the ripples. When both agree, the crowd is unified and moves are powerful.",
            "Decide direction on the higher timeframe (only take longs if the weekly trend is up), then time the "
            "entry on the lower one. Conflicting timeframes = lower conviction, smaller size or skip.")),
    ]),
    ("PART 2 — Price Action & Chart Patterns", [
        ("p2_patterns.png", "Reversal candlestick patterns", block(
            "Doji (indecision), Hammer (bullish reversal), Bullish Engulfing (strong reversal up), Shooting "
            "Star (bearish reversal).",
            "Each captures a sudden shift in the buyer/seller balance at the end of a move, which often precedes "
            "a turn.",
            "<b>Doji</b>: after a strong trend, buyers and sellers reach equilibrium — the side that was winning "
            "has lost control. <b>Hammer</b>: in a downtrend, sellers drive price far down but buyers storm in and "
            "close near the high — sellers are now trapped and must cover, fuelling a bounce. <b>Bullish "
            "engulfing</b>: sellers open confidently lower, then buyers overwhelm them and close above the entire "
            "prior candle — a visible sentiment flip that traps shorts. <b>Shooting star</b>: buyers make a new "
            "high but sellers reject it hard — demand is exhausted.",
            "Only act on these AT a level (support/resistance/MA) and ideally with above-average volume — that "
            "confluence is what makes them reliable rather than random.",
            "Stress that a candle in mid-air means little; the SAME candle at a major support with high volume is "
            "a high-probability signal because trapped traders are forced to act.")),
        ("02_patterns.png", "Trading a reversal — the hammer buy (worked example)", block(
            "A step-by-step example of trading ONE reversal candle: a hammer that appears at support.",
            "The hammer shows sellers tried to push lower but buyers won the day back — the first sign of a turn.",
            "Sellers who shorted the lows are now trapped; as price rises they're forced to buy back, adding fuel.",
            "Wait for the NEXT candle to close above the hammer's high before buying — that confirms it; stop "
            "just below the hammer, target the next resistance.",
            "Never trade a hammer floating in mid-air — it only counts at a level like support.")),
        ("p2_star.png", "Three-candle star reversals", block(
            "Morning Star (bullish bottom) and Evening Star (bearish top) — a trend candle, a small 'star' of "
            "indecision, then a strong candle the other way.",
            "They show a three-act transfer of control: dominance, hesitation, then reversal — more reliable "
            "than a single candle because the shift is confirmed over three sessions.",
            "Act 1: the trend looks healthy. Act 2: the small star shows the dominant side suddenly can't push "
            "further (doubt creeps in). Act 3: the opposite side seizes control with conviction. The pause is the "
            "moment the crowd's belief cracks.",
            "Enter on the third candle's confirmation; place the stop beyond the star's extreme.")),
        ("04_support_resistance.png", "Support & resistance — the floor and the ceiling", block(
            "Support = a price floor where buyers repeatedly step in; resistance = a ceiling where sellers "
            "repeatedly step in.",
            "They work because of MEMORY and order clustering: traders remember prices where reversals happened "
            "and place orders there again, which makes the level hold — partly self-fulfilling.",
            "At support three groups buy at once: those who missed the last rally and want a second chance, those "
            "who bought there before and add, and shorts taking profit. That clustered demand stops the fall. "
            "<b>Role reversal</b>: when resistance finally breaks, traders who sold there are now trapped at a loss "
            "and buy back at breakeven on the retest — turning old resistance into new support.",
            "Buy near support / sell near resistance with a stop just beyond the level; trade the breakout when "
            "price clears it on strong volume.",
            "The more times a level is tested the more significant it is — but each test consumes orders, so a "
            "level tested many times eventually breaks (the supply/demand there gets used up).")),
        ("p2_trendlines.png", "Trendlines", block(
            "A line connecting the rising lows of an uptrend (or falling highs of a downtrend); a sloping "
            "support/resistance.",
            "It visualises that buyers are consistently willing to step in at HIGHER prices each time — proof of "
            "increasing demand.",
            "Each bounce off the line is buyers showing growing optimism (paying up earlier each dip). A break "
            "of the line means that rising demand has finally failed — the psychological 'agreement' to keep "
            "buying higher has broken.",
            "Needs two touches to draw, a third to confirm. Buy bounces off the line in an uptrend; treat a "
            "decisive break as an early warning to tighten stops.")),
        ("p2_headshoulders.png", "Head & Shoulders (top reversal)", block(
            "Three peaks — a higher middle peak (head) between two lower peaks (shoulders) — with a 'neckline' "
            "support; a break below it signals a top.",
            "It maps a trend visibly running out of buyers: each rally attempt has less force, and the final "
            "support break unleashes trapped longs.",
            "Left shoulder = a normal rally with healthy volume. Head = a euphoric push to a new high but usually "
            "on LOWER volume — the last greedy buyers. Right shoulder = buyers try again but can't even make a new "
            "high — demand is exhausted. When the neckline breaks, everyone who bought the top is underwater and "
            "sells, accelerating the fall.",
            "Sell on the neckline break (ideally a retest of it from below); target ≈ the head-to-neckline "
            "distance projected down. Volume should fall through the head and spike on the break.",
            "The volume signature is the tell — point out that lower volume on the head vs the left shoulder "
            "reveals weakening conviction even before the break.")),
        ("p2_double_bottom.png", "Double Bottom (W) — reversal up", block(
            "Price falls to a level, bounces, falls to the SAME level again, then bounces — a 'W' shape.",
            "A level that holds twice proves strong buying support sits there; the second hold convinces sellers "
            "to give up.",
            "Sellers attack the low twice and fail both times — they realise demand won't break, so selling dries "
            "up and the reversal begins. Sellers who shorted the second dip get trapped and must buy back.",
            "BUY when price closes above the middle bounce high (the neckline); stop below the bottoms; target = "
            "the pattern's height added to the breakout point.")),
        ("p2_double_top.png", "Double Top (M) — reversal down", block(
            "Price rises to a level, pulls back, rises to the SAME level again, then falls — an 'M' shape.",
            "A ceiling that rejects price twice proves strong selling supply; the second failure makes buyers give up.",
            "Buyers push the high twice and fail — they realise supply won't break, so buying dries up and the "
            "decline begins. Buyers who chased the second push get trapped and bail.",
            "SELL when price closes below the middle pullback low (the neckline); stop above the tops; target = "
            "the pattern's height below the breakdown.")),
        ("p2_tri_ascending.png", "Ascending Triangle — usually breaks UP", block(
            "A flat resistance line on top with rising lows underneath, squeezing into the corner.",
            "Buyers keep paying higher prices (rising lows) while sellers defend one ceiling — eventually buyers "
            "absorb all the supply and break out.",
            "The rising lows show growing, impatient demand; the flat top is a wall of sell orders. When that wall "
            "is finally eaten through, trapped sellers plus FOMO buyers fuel the upside break.",
            "BUY the breakout above the flat top, ideally on a volume surge; stop just inside the triangle; target "
            "= the triangle's height added to the breakout.")),
        ("p2_tri_descending.png", "Descending Triangle — usually breaks DOWN", block(
            "A flat support line on the bottom with falling highs above, squeezing downward.",
            "Sellers keep accepting lower prices (falling highs) while buyers defend one floor — eventually sellers "
            "break it.",
            "Falling highs show weakening demand; the flat bottom is a shrinking wall of buy orders. When it "
            "breaks, trapped buyers bail and the decline accelerates.",
            "SELL the breakdown below the flat bottom; stop just inside the triangle; target = the triangle's "
            "height below the breakdown.")),
        ("p2_tri_symmetric.png", "Symmetrical Triangle — breaks WITH the trend", block(
            "Both lines converge — lower highs AND higher lows squeezing to a point.",
            "Buyers and sellers both compress; the breakout reveals whose conviction was real — usually the prior "
            "trend wins.",
            "It's a coiled spring of indecision; volatility contracts to a calm, then releases violently once one "
            "side finally gives way.",
            "Trade the breakout in its direction (favour the prior trend), ideally with volume; stop on the "
            "opposite side; target = the triangle's widest height.")),
        ("p2_flag.png", "Bull Flag — continuation up", block(
            "A sharp rally (the 'flagpole'), then a small sideways/down drift (the 'flag'), then another leg up.",
            "Strong moves pause to let early buyers take profit; once weak hands are out, the dominant buyers resume.",
            "The pullback shakes out nervous holders while the big players stay put — so the trend continues after "
            "the breather.",
            "BUY the breakout above the flag; stop below the flag low; target = the flagpole height added to the "
            "breakout point.")),
        ("p2_cup.png", "Cup & Handle — continuation up", block(
            "A rounded 'U' base (the cup), then a small dip (the handle), then a breakout upward.",
            "The rounded bottom shows sentiment slowly shifting from selling to buying; the handle is a final shakeout.",
            "Despair fades to hope across the cup; the small handle dip flushes the last weak holders right before "
            "the breakout.",
            "BUY the breakout above the handle's high; stop below the handle; target = the cup's depth added to "
            "the breakout point.")),
        ("p2_gaps.png", "Gaps", block(
            "Empty space on the chart where price opens far from the previous close — usually on overnight news.",
            "A gap marks a sudden supply/demand imbalance strong enough that no trading happened in between.",
            "Gaps are pure emotion crystallised: a breakaway gap = new information genuinely repricing the asset; "
            "an exhaustion gap = the last euphoric buyers or panicked sellers piling in at the end of a move. Many "
            "gaps 'fill' later because the initial reaction was an emotional overshoot that rational traders fade.",
            "Breakaway gaps (with volume) often start strong trends — trade with them; exhaustion gaps often mark "
            "ends — fade them. Watch for the gap to fill as a target.")),
    ]),
    ("PART 3 — Indicators (and why each works)", [
        ("05_moving_averages.png", "Moving averages", block(
            "The average closing price over the last N days, re-plotted daily, smoothing out noise.",
            "It represents the average price participants paid recently — a moving 'consensus value' that the "
            "market gravitates around.",
            "When price is above the MA, the average holder is in profit and feels confident (bullish bias); "
            "below it, holders are underwater and nervous. Traders treat the MA as a fair-value reference and buy "
            "dips to it, which is why it acts as dynamic support. A golden cross (fast above slow) means the "
            "recent average cost has risen above the long-term — sentiment has structurally turned up.",
            "Use price-vs-MA for trend bias and MA crossovers for shifts; the 20/50/200-day are the most-watched "
            "(self-fulfilling because everyone uses them).")),
        ("06_rsi.png", "RSI — overbought / oversold", block(
            "A 0–100 oscillator measuring the strength of recent gains versus losses (default 14 periods).",
            "It quantifies momentum — how one-sided the buying or selling has been — so you can spot when a move "
            "is overstretched.",
            "Above 70 (overbought) means buying has been so aggressive that nearly everyone who wanted in is "
            "already in — there's little fuel left, so a pause/pullback is likely. Below 30 (oversold) means "
            "panic selling has likely exhausted itself. <b>Divergence</b> is the deeper signal: if price makes a "
            "new high but RSI doesn't, the rally is being driven by fewer and weaker buyers — momentum is dying.",
            "Use it as a warning light, not a trigger; in strong trends RSI can stay extreme for a long time, so "
            "combine it with price action.",
            "Emphasise that 'overbought' ≠ 'sell now' — in a powerful uptrend shorting overbought RSI is a "
            "classic beginner mistake; divergence is the higher-quality signal.")),
        ("06b_rsi_divergence.png", "RSI Divergence — the early reversal warning", block(
            "When price and the RSI line disagree — price makes a new high but RSI makes a lower high "
            "(or price makes a new low but RSI makes a higher low).",
            "RSI is built from momentum, so it can reveal that a new price high was made on weaker buying — "
            "the move is running on fumes before price actually turns.",
            "The crowd sees a fresh high and feels safe; the divergence quietly shows momentum fading "
            "underneath — smart money is often selling into that strength.",
            "Confirm with a price break (a close below a recent swing low) before acting — divergence warns, "
            "price triggers.",
            "Regular divergence warns of a reversal; hidden divergence signals trend continuation.")),
        ("07_macd.png", "MACD — trend + momentum", block(
            "The gap between a fast (12) and slow (26) EMA, with a 9-EMA signal line and a histogram of the gap.",
            "It captures the rate at which the short-term average is pulling away from the long-term — i.e., "
            "accelerating or fading momentum.",
            "A bullish crossover means short-term buying pressure has overtaken the longer-term trend — the "
            "balance of power is shifting to buyers in real time. The histogram shrinking even while price rises "
            "warns that momentum is fading before price actually turns.",
            "Use crossovers for entries/exits and histogram + divergence for early warnings; best as confirmation "
            "alongside trend and levels.")),
        ("p3_stochastic.png", "Stochastic oscillator", block(
            "Shows where the close sits within the recent high-low range (0–100), with %K and %D lines.",
            "Closing near the top of the range signals strength; near the bottom, weakness — a quick read on "
            "momentum, especially in ranges.",
            "In an uptrend price tends to close near its highs (confident buyers); when it starts closing in the "
            "lower part of the range despite higher prices, buyers are tiring. Overbought/oversold zones flag "
            "emotional extremes in range-bound markets.",
            "Best in sideways markets; use %K/%D crossovers in the 80/20 zones, and watch for divergence.")),
        ("p3_adx.png", "ADX — trend STRENGTH", block(
            "A 0–100 line measuring how strong a trend is, regardless of direction.",
            "Many tools only work in the right regime — ADX tells you whether to use trend tools or range tools.",
            "A high ADX means participants broadly agree on direction (strong conviction, persistent trend); a "
            "low ADX means disagreement/indecision (choppy range). It's a measure of crowd consensus strength.",
            "Above 25 → trade with the trend (let winners run); below 20 → switch to range tactics (fade extremes). "
            "Don't use RSI overbought-as-sell when ADX is high — the trend will keep pushing.")),
        ("08_bollinger.png", "Bollinger Bands — volatility", block(
            "A 20-day average with bands set 2 standard deviations above and below it.",
            "Two standard deviations statistically contain ~95% of recent prices, so touches of the bands flag "
            "stretched conditions, and band WIDTH measures volatility.",
            "A 'squeeze' (very narrow bands) reflects low disagreement and complacency — a coiled spring; when "
            "new information arrives, the pent-up move releases violently (expansion). Price hugging the upper "
            "band shows persistent strength, not just 'overbought'.",
            "Trade squeeze breakouts in the breakout direction; in a range, fade band touches back to the middle "
            "average.")),
        ("p3_atr.png", "ATR — how much it moves", block(
            "Average True Range — the typical size of a day's move, including gaps (pure volatility, no direction).",
            "Risk must be scaled to volatility; ATR gives you that yardstick objectively.",
            "Volatility is emotional intensity — ATR rises when fear/excitement spikes. A stop placed without "
            "regard to ATR will be too tight in a volatile name (stopped out by noise) or too loose in a calm one.",
            "Set stops at ~1.5–2× ATR from entry and size positions so each trade risks a similar rupee amount "
            "regardless of the asset's volatility.")),
        ("p3_volume.png", "Volume — the fuel", block(
            "The number of shares/contracts traded; shown as bars under price.",
            "Price tells you the direction; volume tells you the conviction behind it.",
            "A big move on heavy volume means many participants agree — real money is committed, so it's likely "
            "to continue. The same move on thin volume means few believe it; it's fragile and often reverses. "
            "Rising volume into a breakout confirms genuine demand.",
            "Demand volume confirmation on breakouts; be sceptical of moves and patterns that complete on weak "
            "volume.")),
        ("09_fibonacci.png", "Fibonacci retracement", block(
            "Horizontal levels at 23.6%, 38.2%, 50% and 61.8% of a prior move, marking likely pullback zones.",
            "It works through a mix of natural profit-taking rhythm and self-fulfilment — so many traders watch "
            "these levels that orders cluster there.",
            "After a rally, some buyers take profit, causing a dip. The 38.2–61.8% zone is where the pullback has "
            "given back enough to shake out weak hands and tempt new buyers who missed the move — so demand "
            "re-emerges there. A 61.8% retracement is the deepest 'healthy' pullback before the trend is in doubt.",
            "In an uptrend, buy dips into the 38–62% zone, especially where a Fib level lines up with support or a "
            "moving average (confluence = higher probability).")),
        ("p3_pivots.png", "Pivot points", block(
            "Support (S1, S2) and resistance (R1, R2) levels auto-calculated from the prior day's high, low and "
            "close, around a central pivot.",
            "They give objective intraday reference levels derived from where the market just agreed value was.",
            "Because day-traders and algos all compute the same pivots, orders cluster at them — they become "
            "self-fulfilling intraday magnets and barriers. Price above the central pivot = bullish bias for the "
            "session.",
            "Use them for intraday targets and stops on indices and F&O; trade bounces/rejections at S/R levels "
            "and breakouts through them.")),
    ]),
    ("PART 4 — Theories", [
        ("p4_divergence.png", "Divergence — the hidden warning", block(
            "Price and a momentum indicator (RSI/MACD) disagree — e.g., price makes a higher high but the "
            "indicator makes a lower high.",
            "Price can keep rising on diminishing participation; the indicator exposes that the engine is "
            "weakening before the car stops.",
            "A new price high on weaker momentum means the rally is being carried by fewer, later, and smaller "
            "buyers — often smart money is quietly distributing to an euphoric crowd. The crowd sees a new high "
            "and feels safe; the divergence reveals the opposite.",
            "Treat divergence as an early-warning to tighten stops or look for a reversal trigger — not a "
            "stand-alone sell; wait for price confirmation (a break of support).",
            "Distinguish regular divergence (warns of reversal) from hidden divergence (signals trend "
            "continuation) — mentioning both shows real depth.")),
        ("03_trend.png", "Trend structure", block(
            "Uptrend = higher highs and higher lows; downtrend = lower highs and lower lows; sideways = a range.",
            "Trends persist because of feedback loops — rising prices attract more buyers and validate holders, "
            "which pushes prices higher still.",
            "An uptrend is a visible story of growing optimism: each dip is bought earlier (higher lows = "
            "impatient demand) and each push reaches further (higher highs). The trend ends when that optimism "
            "breaks — the first lower high/low signals the psychology has shifted.",
            "Always define the trend first and trade with it: buy dips in uptrends, sell rallies in downtrends, "
            "stand aside in choppy ranges.")),
        ("p4_elliott.png", "Elliott Wave", block(
            "Trends unfold in 5 waves in the trend direction (1-3-5 up, 2-4 pullbacks), then correct in 3 waves "
            "(A-B-C).",
            "It formalises the natural swing of crowd emotion between optimism and pessimism, and is fractal "
            "(the same shape on every timeframe).",
            "Wave 1 = a few early believers. Wave 2 = doubt (pullback). Wave 3 = the crowd recognises the trend — "
            "the strongest, longest wave (peak optimism building). Wave 4 = profit-taking. Wave 5 = euphoria/"
            "exhaustion, often on divergence. Then A-B-C unwinds the excess as reality sets in.",
            "Use it to gauge where a move is in its life-cycle — e.g., be cautious chasing a 'wave 5' that shows "
            "momentum divergence. Acknowledge it's subjective and best combined with other tools.")),
    ]),
    ("PART 5 — Futures & Options (F&O)", [
        ("p5_futures_curve.png", "Futures: contango vs backwardation", block(
            "The shape of futures prices across expiries — contango (futures above spot) or backwardation "
            "(futures below spot).",
            "The curve reflects the cost of carrying the asset versus how urgently the market wants it now.",
            "Contango is 'normal' — futures cost more because of interest/storage (cost of carry). Backwardation "
            "signals near-term scarcity or strong immediate demand — buyers will pay a premium for the asset NOW "
            "rather than later (common in tight crude/commodity markets), a sign of bullish urgency.",
            "Watch the curve and rollovers: heavy long rollover to the next expiry signals trend conviction; "
            "backwardation often accompanies strong spot demand.")),
        ("p5_call.png", "Long Call — bet that price will RISE", block(
            "A call gives you the right (not obligation) to BUY at a fixed strike price. You pay a premium; that "
            "premium is your maximum loss.",
            "It gives leveraged upside with limited, known risk — a small premium controls a large position.",
            "The buyer pays a little for a big potential payoff (asymmetric) — attractive when you're confident "
            "price will rise. The seller collects the premium and bets it won't.",
            "BUY a call when bullish and your setup triggers; exit at your target or cut if the underlying breaks "
            "your stop. Time decay (theta) eats value daily, so don't overstay.")),
        ("p5_put.png", "Long Put — bet that price will FALL", block(
            "A put gives you the right to SELL at a fixed strike price. You pay a premium; that premium is your "
            "maximum loss.",
            "It profits as price falls, with limited risk — a way to go bearish or to hedge a holding.",
            "The buyer pays a small premium for large downside profit; it's also 'insurance' for someone who owns "
            "the stock and fears a drop.",
            "BUY a put when bearish, or to protect a holding; exit at target or if the underlying reclaims your "
            "level. Theta works against you each day.")),
        ("p5_covered_call.png", "Covered Call — earn income on a holding", block(
            "You OWN the stock and SELL a call against it, collecting the premium as income.",
            "It turns a flat/mildly-bullish holding into income, in exchange for capping your upside.",
            "A mildly bullish, income-seeking mindset: you're happy to give up big upside for a steady premium "
            "while you hold the stock.",
            "Use it on stocks you already own and expect to move sideways; you keep the premium if price stays "
            "below the strike, but your gains are capped above it.")),
        ("p5_straddle.png", "Long Straddle — bet on a BIG move either way", block(
            "Buy a call AND a put at the SAME strike. You profit if price moves sharply in EITHER direction.",
            "It's a pure volatility bet — direction doesn't matter, only the size of the move.",
            "The buyer doesn't care up or down, only that something big happens — typically bought before events "
            "(results, budget) when a large move is expected but the direction is unknown.",
            "BUY before a known event; you need a move bigger than the combined premium to profit. Exit fast after "
            "the event — volatility (IV) collapses and theta accelerates.")),
        ("p5_bull_spread.png", "Bull Call Spread — cheaper bullish bet", block(
            "Buy a call AND sell a higher-strike call. This caps both your cost and your reward.",
            "It expresses a moderate bullish view for less money than a naked call, with a known maximum loss.",
            "A disciplined, probability-minded approach: you accept a capped reward in exchange for lower cost and "
            "defined risk.",
            "Use when you expect a moderate rise (not a moonshot); max profit near the higher strike, max loss = "
            "the net premium paid.")),
        ("p5_iron_condor.png", "Iron Condor — profit when price goes NOWHERE", block(
            "Sell an out-of-the-money call spread AND put spread. You profit if price stays in a range.",
            "It monetises a calm, range-bound market by collecting premium that decays with time.",
            "The seller is betting on quiet markets and harvests time decay as long as price stays inside the "
            "range — effectively selling 'insurance' to nervous traders.",
            "Use when you expect low volatility; close at ~50% of max profit rather than holding to expiry. The "
            "danger is a sudden breakout beyond your short strikes.")),
        ("p5_oi_chain.png", "Open Interest & the option chain", block(
            "Open Interest = number of outstanding contracts at each strike, displayed across the option chain.",
            "It shows where large positions (often institutional writers) are concentrated, which creates "
            "magnetic support/resistance.",
            "The strike with the highest CALL open interest tends to act as resistance — call writers (who "
            "collected premium) defend it and want price to stay below. Highest PUT open interest acts as support "
            "for the same reason. <b>Max pain</b> is the strike where the most options expire worthless, and price "
            "often drifts there near expiry because large writers are incentivised to push it.",
            "Read OI to map likely intraday/expiry support and resistance; rising OI + rising price = fresh longs "
            "(strong), rising OI + falling price = fresh shorts.",
            "Mention PCR (put-call ratio) as a sentiment gauge — a very high PCR can be contrarian bullish "
            "(excessive fear).")),
        ("p5_iv_skew.png", "Implied Volatility & skew", block(
            "IV is the market's expected future volatility implied by option prices; skew = IV differing across "
            "strikes.",
            "Option prices reveal what the crowd expects volatility to be — fear and demand for protection get "
            "priced in.",
            "Downside puts usually carry higher IV (the 'skew') because investors fear crashes more than melt-ups "
            "and pay up for protection — a measurable fingerprint of fear. High overall IV means options are "
            "expensive (lots of expected movement / anxiety); low IV means complacency.",
            "Buy options when IV is low and sell premium when IV is high; reading the IV surface (across strikes "
            "and expiries) is exactly the volatility-analysis work you did on the desk.")),
    ]),
    ("PART 6 & 7 — Commodities, Indices & Sentiment", [
        ("p6_gold_dollar.png", "Gold vs the US Dollar", block(
            "Gold (priced in USD) and the US Dollar Index usually move in opposite directions.",
            "Because gold is priced in dollars and competes with the dollar as a store of value, a stronger "
            "dollar mechanically and psychologically weakens gold.",
            "Gold pays no interest, so when real yields/the dollar rise, money prefers cash/bonds and gold falls. "
            "In fear or high inflation, investors flee to gold as a safe haven and inflation hedge — gold rises on "
            "anxiety. It's a barometer of distrust in paper money.",
            "Track the dollar, real yields and risk sentiment when forming a gold view; crude instead keys off "
            "OPEC supply, global demand and geopolitics.")),
        ("p7_vix.png", "India VIX — the fear gauge", block(
            "VIX measures the market's expected 30-day volatility, derived from index option prices.",
            "When traders expect big moves they pay up for options, which pushes VIX up — so it reads collective "
            "anxiety.",
            "VIX spikes during selloffs because fear drives a rush to buy protective puts. Extreme VIX often "
            "coincides with capitulation bottoms (peak fear = sellers exhausted); very low VIX signals complacency "
            "and can precede sharp shocks.",
            "Use VIX as a contrarian sentiment tool — spikes near support can flag bounce opportunities; "
            "persistently low VIX warns against complacency.")),
    ]),
    ("PART 8 — Risk Management (what makes a pro)", [
        ("p8_riskreward.png", "Risk : Reward and stops", block(
            "Every trade defined by an entry, a stop-loss (exit if wrong) and a target, with reward sized larger "
            "than risk.",
            "Positive expectancy doesn't require being right often — it requires winners bigger than losers.",
            "The stop-loss exists to defeat loss aversion — the human urge to hold losers hoping they recover, "
            "which turns small losses into account-killers. Pre-deciding the exit removes emotion in the heat of "
            "the moment. A 1:2+ reward:risk means you can be wrong more than half the time and still grow capital.",
            "Demand at least 2:1 reward:risk, set the stop at a level that invalidates your idea (not an arbitrary "
            "%), and never move a stop further away to avoid being wrong.",
            "Frame it as 'survive first': controlling the downside is what keeps you in the game long enough for "
            "your edge to play out.")),
        ("p8_drawdown.png", "Drawdown — the pain measure", block(
            "Drawdown is the fall from an equity peak; max drawdown is the worst such fall a strategy/account "
            "suffered.",
            "Returns alone are meaningless without knowing the pain endured to get them — drawdown measures risk "
            "of ruin and of quitting.",
            "Big drawdowns break traders psychologically — most abandon a strategy at its worst point, locking in "
            "the loss. A strategy with lower drawdown is one you can actually stick with, which is why "
            "risk-adjusted measures (Sharpe, Sortino) matter more than raw return.",
            "Judge any strategy by drawdown and Sharpe/Sortino, not just total return; size positions so a normal "
            "drawdown is survivable both financially and emotionally.")),
        ("10_setup.png", "Putting it ALL together — a real trade", block(
            "A complete setup: confirm the uptrend, wait for a pullback to support/MA, then buy with a stop just "
            "below and a target above.",
            "It stacks independent edges — trend, level, momentum, and favourable risk:reward — so the "
            "probabilities line up in your favour.",
            "You're buying where the crowd that missed the move re-enters (support), in the direction the "
            "dominant players favour (trend), with a pre-planned exit that keeps emotion out. Each confluence "
            "factor is another group of traders acting in your favour.",
            "Checklist every trade: trend ✓ → level ✓ → trigger (candle/indicator) ✓ → entry, stop, target with "
            "reward > risk. If any piece is missing, pass.")),
    ]),
]


def b64(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()


def main():
    parts_html = []
    for part_title, items in PARTS:
        parts_html.append(f'<h1>{part_title}</h1>')
        for img, head, text in items:
            p = os.path.join(IMG, img)
            if not os.path.exists(p):
                continue
            dd = DEEP.get(img)
            if dd:
                text = text + f'<br><span class="deep">{dd}</span>'
            tp = TRADE_PLANS.get(img)
            if tp:
                text = text + trade_plan_html(*tp)
            parts_html.append(f"""
            <div class="card">
              <div class="keep"><h2>{head}</h2><img src="{b64(p)}"/></div>
              <p>{text}</p>
            </div>""")
    body = "\n".join(parts_html)

    # merge the remaining text topics + names + formulas into the SAME document
    ref_html = ""
    ref_md = ""
    sup_path = os.path.join(MD, "SUPPLEMENT.md")   # PARTS 9-13 (theory, regulation, psychology, tools)
    if os.path.exists(sup_path):
        with open(sup_path, encoding="utf-8") as f:
            ref_md += f.read() + "\n\n"
    md_path = os.path.join(MD, "NAMES_AND_FORMULAS.md")
    if os.path.exists(md_path):
        with open(md_path, encoding="utf-8") as f:
            md = f.read()
        md = md.replace("# PART 1 — THE STORY BEHIND EVERY NAME",
                        "# PART 14 — The Story Behind Every Name (memory hooks)")
        md = md.replace("# PART 2 — THE FORMULAS (with worked examples)",
                        "# PART 15 — Formulas & Worked Examples")
        cut = md.find("# PART 14")
        if cut > 0:
            md = md[cut:]
        ref_md += md
    # interview crash course -> PART 16 (lives in the resumes root folder)
    sg_path = os.path.join(MD, "INTERVIEW_PREP_STUDY_GUIDE.md")
    if os.path.exists(sg_path):
        with open(sg_path, encoding="utf-8") as f:
            sg = f.read()
        idx = sg.find("\n## ")            # drop the study guide's own title/intro block
        if idx > 0:
            sg = sg[idx + 1:]
        sg = re.sub(r'(?m)^## ', '### ', sg)   # demote its h2 sections to h3 under PART 16
        ref_md += ("\n\n# PART 16 — Interview Prep: Self-Intro, Rapid Revision & Q&A\n\n" + sg)
    if ref_md:
        ref_body = markdown.markdown(ref_md, extensions=["tables", "fenced_code", "sane_lists"])
        ref_html = f'<div class="ref">{ref_body}</div>'

    html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
      @page {{ size: A4; margin: 12mm 13mm; }}
      * {{ box-sizing: border-box; }}
      body {{ font-family:"Calibri","Segoe UI",sans-serif; color:#1a1a1a; }}
      .cover {{ text-align:center; padding-top:40px; }}
      .cover h1 {{ color:#16365c; font-size:24pt; border:none; }}
      .cover p {{ color:#555; font-size:11pt; }}
      h1 {{ color:#16365c; font-size:16pt; border-bottom:2.4px solid #16365c; padding-bottom:4px;
            margin:16px 0 8px; page-break-before:always; }}
      .card {{ margin-bottom:16px; border:1px solid #dfe5ee; border-radius:7px; padding:9px 13px;
               page-break-inside:avoid; }}
      .keep {{ page-break-inside:avoid; }}
      .card h2 {{ color:#16365c; font-size:13pt; margin-bottom:5px; }}
      .card img {{ width:100%; border:1px solid #eee; border-radius:5px; }}
      .card p {{ font-size:10.2pt; line-height:1.5; margin-top:8px; }}
      .card p b {{ color:#16365c; }}
      .plan {{ display:block; margin-top:8px; padding:8px 11px; background:#eafaf0;
               border-left:4px solid #1a7f37; border-radius:5px; }}
      .plan b {{ color:#14622e; }}
      .deep {{ display:block; margin-top:8px; padding:8px 11px; background:#eef4fb;
               border-left:4px solid #1f4e79; border-radius:5px; }}
      .deep b {{ color:#143055; }}
      .deep code {{ background:#dde7f3; padding:1px 4px; border-radius:3px; font-size:9.4pt; }}
      /* reference sections (names tables + formulas) */
      .ref {{ font-size:10.2pt; line-height:1.45; }}
      .ref h3 {{ color:#22364f; font-size:11pt; margin:11px 0 3px; }}
      .ref p {{ margin:5px 0; }}
      .ref ul, .ref ol {{ margin:4px 0 8px 22px; }}
      .ref strong {{ color:#143055; }}
      .ref blockquote {{ background:#f4f7fb; border-left:3px solid #16365c; margin:6px 0; padding:6px 12px; color:#333; }}
      .ref table {{ border-collapse:collapse; width:100%; font-size:9.5pt; margin:8px 0; page-break-inside:avoid; }}
      .ref th {{ background:#16365c; color:#fff; text-align:left; padding:5px 8px; }}
      .ref td {{ padding:4px 8px; border-bottom:1px solid #e3e8ef; vertical-align:top; }}
      .ref tr:nth-child(even) td {{ background:#f6f8fb; }}
      .ref code {{ background:#eef2f7; padding:1px 4px; border-radius:3px; font-size:9.3pt; }}
      .ref pre {{ background:#f4f7fb; padding:8px 12px; border-radius:5px; white-space:pre-wrap;
                  font-size:9.3pt; page-break-inside:avoid; }}
      .ref hr {{ border:none; border-top:1px solid #d0d7e2; margin:10px 0; }}
    </style></head><body>
      <div class="cover">
        <h1>Technical Analysis<br>Illustrated Handbook</h1>
        <p>Every topic: the chart, why it works, and the market psychology behind it.<br>
        Built to answer the interviewer's follow-up question.<br><br>
        Prepared for Saikumar Kaleru — Technical Research Analyst prep</p>
      </div>
      {body}
      {ref_html}
    </body></html>"""
    hp = os.path.join(HERE, "_ihb.html")
    with open(hp, "w", encoding="utf-8") as f:
        f.write(html)
    chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    subprocess.run([chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={PDF}", "file:///" + hp.replace("\\", "/")],
                   check=False, stderr=subprocess.DEVNULL)
    os.remove(hp)
    print("PAGES:", fitz.open(PDF).page_count, "->", PDF)


if __name__ == "__main__":
    main()
