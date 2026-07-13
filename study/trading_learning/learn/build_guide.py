"""Compile the annotated charts + beginner explanations into a Visual Learning Guide PDF."""
import os
import base64
import subprocess
import fitz

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "img")
PDF = os.path.join(HERE, "VISUAL_LEARNING_GUIDE.pdf")

# (image file, heading, beginner explanation)
SECTIONS = [
    ("01_anatomy.png", "1. What a candlestick is",
     "Every candle = one day of trading. The thick part is the <b>body</b> (where price opened and "
     "closed). The thin lines are <b>wicks/shadows</b> (the highest and lowest price that day). "
     "<b>Green</b> = price closed higher than it opened (buyers won). <b>Red</b> = closed lower "
     "(sellers won). This is the alphabet of charts — everything else is built on it."),
    ("02_patterns.png", "2. Candlestick patterns that signal reversals",
     "Certain candle shapes warn that the trend may flip. <b>Doji</b> (tiny body) = buyers and "
     "sellers are balanced → indecision. <b>Hammer</b> = a long lower wick after a fall → buyers "
     "stepped in → bullish. <b>Bullish Engulfing</b> = a big green candle swallows the previous red "
     "one → strong reversal up. <b>Shooting Star</b> = long upper wick after a rise → sellers took "
     "over → bearish. These matter most when they appear AT support or resistance."),
    ("03_trend.png", "3. Trend — the single most important thing",
     "An <b>uptrend</b> is a staircase going up: each peak is higher than the last (higher highs) and "
     "each dip is higher too (higher lows). A <b>downtrend</b> is the opposite. The golden rule: "
     "<b>trade WITH the trend</b> — in an uptrend you look to BUY the dips, not short. Most beginner "
     "losses come from fighting the trend."),
    ("04_support_resistance.png", "4. Support & Resistance — the floor and the ceiling",
     "<b>Support</b> is a price level where the fall keeps stopping — buyers reliably step in (a "
     "floor). <b>Resistance</b> is where rises keep stopping — sellers step in (a ceiling). Price "
     "tends to bounce between them. The plan is simple: buy near support, sell near resistance, and "
     "when price <b>breaks</b> through a level decisively, that often starts a new move. Tip: broken "
     "resistance often becomes the new support."),
    ("05_moving_averages.png", "5. Moving Averages — the trend made smooth",
     "A moving average (MA) is just the average price of the last N days, redrawn each day — it "
     "smooths out the noise so you can see the real direction. Price <b>above</b> the MAs = uptrend; "
     "below = downtrend. When the <b>fast</b> MA (20-day) crosses <b>above</b> the <b>slow</b> MA "
     "(50-day) it's bullish (the famous 'golden cross'); crossing below is bearish ('death cross'). "
     "MAs also act as moving support/resistance."),
    ("06_rsi.png", "6. RSI — is the move overstretched?",
     "RSI is a meter from 0 to 100 (shown in the lower panel) that measures momentum. <b>Above 70</b> "
     "= 'overbought' — the rise may be tired and could pull back. <b>Below 30</b> = 'oversold' — the "
     "fall may be overdone and could bounce. It does NOT mean buy/sell instantly — in a strong trend "
     "RSI can stay extreme. Use it as a warning light, not a trigger."),
    ("07_macd.png", "7. MACD — trend + momentum in one",
     "MACD (lower panel) is built from two moving averages. The key signal is the crossover: when the "
     "<b>green MACD line crosses above the red signal line</b>, momentum is turning <b>bullish</b>; "
     "crossing below is bearish. The bars (histogram) show how strong that momentum is — taller bars "
     "= stronger push. It's one of the most-used confirmation tools."),
    ("08_bollinger.png", "8. Bollinger Bands — measuring volatility",
     "Three lines: a middle 20-day average with an upper and lower band that sit 2 standard deviations "
     "away. The bands <b>widen</b> when the market is volatile and <b>squeeze</b> tight when it's calm "
     "— and a tight squeeze often comes right before a big breakout. Price hugging the upper band = "
     "strong; tapping the lower band in a range = possible bounce."),
    ("09_fibonacci.png", "9. Fibonacci Retracement — where pullbacks pause",
     "After a strong move up, price rarely goes straight — it pulls back before continuing. Fibonacci "
     "levels (drawn from the low to the high) mark where that pullback often <b>pauses and reverses</b> "
     "— mainly the 38.2%, 50% and 61.8% levels. Traders watch the <b>38.2–61.8% zone</b> to buy a dip "
     "in an uptrend. 61.8% (the 'golden ratio') is the most-watched line."),
    ("10_setup.png", "10. Putting it all together — a real BUY setup",
     "Here's how an analyst combines everything into one trade. <b>Step 1:</b> confirm an uptrend "
     "(price above the rising 20-MA). <b>Step 2:</b> wait for a pullback to that MA / a support level. "
     "<b>Step 3:</b> BUY there, place a <b>STOP-LOSS</b> just below (your exit if you're wrong), and a "
     "<b>TARGET</b> above. The golden discipline: your potential reward should be bigger than your risk "
     "(aim 2:1). Every single trade needs an entry, a stop, and a target — no exceptions."),
]


def b64(path):
    with open(path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()


def main():
    cards = ""
    for img, head, text in SECTIONS:
        cards += f"""
        <div class="card">
          <h2>{head}</h2>
          <img src="{b64(os.path.join(IMG, img))}"/>
          <p>{text}</p>
        </div>"""
    html = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
      @page {{ size: A4; margin: 12mm 13mm; }}
      * {{ box-sizing: border-box; }}
      body {{ font-family:"Calibri","Segoe UI",sans-serif; color:#1a1a1a; }}
      .title {{ text-align:center; }}
      .title h1 {{ color:#16365c; font-size:20pt; margin-bottom:2px; }}
      .title p {{ color:#555; font-size:10pt; margin-bottom:6px; }}
      .card {{ page-break-inside:avoid; margin-bottom:14px; border:1px solid #dfe5ee;
               border-radius:7px; padding:10px 14px; }}
      .card h2 {{ color:#16365c; font-size:14pt; margin-bottom:6px; }}
      .card img {{ width:100%; border:1px solid #eee; border-radius:5px; }}
      .card p {{ font-size:10.6pt; line-height:1.5; margin-top:8px; }}
      b {{ color:#143055; }}
    </style></head><body>
      <div class="title">
        <h1>Technical Analysis — Visual Learning Guide</h1>
        <p>See it, then read it. Every concept shown on a real chart, explained for a complete beginner.<br>
        Prepared for Saikumar Kaleru</p>
      </div>
      {cards}
      <div class="card" style="background:#f4f7fb">
        <h2>The beginner's checklist (memorise this)</h2>
        <p><b>1.</b> Which way is the <b>trend</b>? (Up = look to buy.) &nbsp;
           <b>2.</b> Where are <b>support &amp; resistance</b>? &nbsp;
           <b>3.</b> What do the <b>candles</b> say at those levels? &nbsp;
           <b>4.</b> Do <b>RSI / MACD</b> agree? &nbsp;
           <b>5.</b> Set <b>entry, stop-loss, target</b> — reward bigger than risk. &nbsp;
           Then you have a trade you can explain.</p>
      </div>
    </body></html>"""
    hp = os.path.join(HERE, "_guide.html")
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
