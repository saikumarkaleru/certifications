# Q&A — Dividend Policy & Payout

A mix of **theory** (with model answers and interview-ready phrasing) and **numerical problems** (fully solved, numbers self-verified). Work the numericals with pen before reading the solution.

---

## Theory

### Q1. Does dividend policy affect firm value? (THEORY)

**Model answer.** In a *perfect market* — no taxes, no transaction costs, symmetric information, fixed investment policy — Modigliani-Miller (1961) proves payout is **irrelevant**. Investors can create a "homemade dividend" by selling shares, or undo an unwanted one by reinvesting, so they won't pay a premium for the firm's packaging. Value flows from the earning power of the assets and the investment policy.

In the **real world**, four frictions make it matter:
- **Taxes** — dividends historically taxed worse and sooner than capital gains → favors buybacks/retention.
- **Signaling** — a dividend change reveals management's private view of sustainable earnings.
- **Clienteles** — investors self-sort by payout preference, so changing policy just churns your base.
- **Agency** — committing to pay out disciplines cash-rich managers (Jensen's free cash flow).

**How to say it:** "How you return cash matters at the margin through frictions; whether your projects beat the cost of capital matters far more."

---

### Q2. Explain the "homemade dividend" argument. (THEORY)

**Model answer.** If an investor wants more income than the firm pays, they **sell** a sliver of shares to manufacture cash. If they want less, they **reinvest** the dividend by buying more. Because they can replicate any payout stream themselves — costlessly in a perfect market — the firm's payout choice adds no value. Example: owning 1% of a ₹1,000 firm = ₹10. A ₹100 dividend gives ₹1 cash + ₹9 stock. No dividend but selling ₹1 of stock gives ₹1 cash + ₹9 stock. **Identical.** The argument breaks when selling has transaction costs or triggers taxes — which is where real dividend policy lives.

---

### Q3. Dividend vs buyback — how do you advise a client returning cash? (THEORY)

**Model answer.** Four lenses:
1. **Sustainability of the surplus** — recurring → dividend (credible commitment); lumpy/uncertain → buyback (flexible, no cut risk).
2. **Taxes** — buyback usually more efficient: only sellers taxed, as capital gains, on their own timing.
3. **Valuation** — only buy back if shares are at/below intrinsic value; repurchasing overvalued stock transfers value from remaining holders to sellers.
4. **Signal & shareholder base** — a dividend/hike signals permanence and suits an income clientele; a buyback signals "we're undervalued."

**Bottom line:** mature firm + stable cash + income base → dividend; lumpy cash + belief it's cheap → buyback. Many firms do a stable base dividend + opportunistic buybacks.

---

### Q4. What is the information/signaling content of dividends? (THEORY)

**Model answer.** Managers know more than the market. Because dividends are **sticky** and cutting them is punished, setting or raising one is a **credible, costly-to-fake signal** that management believes the higher cash flow is permanent. Hence: increases → price up; cuts/omissions → price down, often by more than the cash impact, because of the negative information revealed. Markets react to the **change**, not the level.

---

### Q5. Explain the clientele effect and its main implication. (THEORY)

**Model answer.** Investors self-sort into stocks whose payout matches their tax status and income needs: tax-exempt funds and retirees gravitate to high payers; high-bracket individuals and growth investors to low payers. **Implication:** a stable clientele already owns your stock, so *changing* policy mainly forces them to churn and incur taxes/costs — it doesn't create value. This is a core reason firms keep payout policy **stable**, and it means the marginal investor is roughly tax-neutral, muting the pure tax argument.

---

### Q6. What is the bird-in-the-hand argument, and is it valid? (THEORY)

**Model answer.** It claims investors prefer certain near-term dividends to uncertain future gains, so higher payout lowers the required return and raises value (Gordon/Lintner). It is **analytically wrong**: paying a dividend does not change the risk of the firm's underlying cash flows — the discount rate reflects asset/business risk, not whether returns arrive as dividends or capital gains. MM and the clientele effect both refute it. Say: "Intuitively appealing, but a dividend doesn't de-risk the business."

---

### Q7. Walk through the effect of a ₹100 cash dividend on the three statements. (THEORY)

**Model answer.**
- **Income statement:** no effect — a dividend is a distribution of after-tax profit, *not* an expense.
- **Cash flow statement:** Cash Flow from Financing −₹100.
- **Balance sheet:** Cash −₹100 (assets); Retained Earnings −₹100 (equity). Balances.
- If **declared but unpaid:** at declaration, Retained Earnings −₹100 and Dividends Payable +₹100 (current liability); the cash outflow hits at the payment date.

**Contrast — a ₹100 buyback:** IS no direct effect (future EPS rises via lower share count); CFF −₹100; BS cash −₹100 and equity −₹100 (treasury stock / retirement).

---

### Q8. Do buybacks always increase EPS and create value? (THEORY)

**Model answer.** Mechanically, fewer shares raise EPS — but the firm spent cash that was earning a return, or borrowed at a cost. A buyback is **accretive only if the after-tax cost of the cash used is below the stock's earnings yield (E/P)**. Buying a high-P/E (low earnings-yield) stock with expensive debt can be **dilutive**. And even when accretive, higher EPS is **not new value** — it's the same earnings over fewer shares; the P/E adjusts. Never claim buybacks are automatically good.

---

### Q9. What is a residual dividend policy, and why don't firms actually follow it? (THEORY)

**Model answer.** Residual policy pays out only what's **left after funding all positive-NPV projects** at the target capital structure: Dividend = Net Income − (equity % × capital budget). It's theoretically clean — never raises costly external equity just to fund a dividend. But because investment opportunities fluctuate, the dividend becomes **erratic** year to year, which markets dislike (it garbles the signal and disrupts clienteles). So firms use residual logic to set a **long-run target payout** and then **smooth** (Lintner partial adjustment) around it.

---

### Q10. Summarize Lintner's stylized facts about dividends. (THEORY)

**Model answer.** (1) Firms target a **long-run payout ratio**. (2) Managers focus on the **change**, not the level. (3) Dividends are **smoothed** — firms only partially adjust toward target each year (speed of adjustment ~0.3–0.5). (4) Managers are **very reluctant to cut** and won't raise unless confident the new level is sustainable. Net effect: dividends look like a slowly rising staircase while earnings zig-zag.

---

### Q11. Why does the share price drop on the ex-dividend date? (THEORY)

**Model answer.** On the ex-date the stock trades **without** the right to the declared dividend. A buyer that day won't receive it, so they only pay a price excluding it — the price falls by roughly the dividend (exactly, in a tax-free world). No value is created or destroyed: ₹X simply moves from firm value into shareholders' cash. Know the sequence: **declaration → ex-date → record date → payment date.**

---

### Q12. A stock yields 11% and the dividend exceeds free cash flow. What do you conclude? (THEORY)

**Model answer.** Red flag for **sustainability / possible value trap**. A payout above free cash flow means the dividend is funded by debt, asset sales, or the cash balance — not operations. I'd examine the multi-year FCF-payout ratio, leverage, and covenant headroom, and treat cut risk as elevated. A high yield driven by a falling price often *precedes* a cut. Sustainable payout must be funded by **recurring free cash flow**, and growth is capped by g = b × ROE.

---

### Q13. When is it rational for a firm to pay no dividend at all? (THEORY)

**Model answer.** When it has abundant **positive-NPV projects with ROE > cost of equity** — retention creates value there (every retained rupee earns the spread, and g = b × ROE). Young high-growth firms rationally pay nothing (Amazon's first dividend came only in 2024). Also when liquidity is tight, covenants restrict payouts, or the firm wants to avoid the tax/clientele cost of a dividend it might have to cut.

---

## Numerical

### Q14. Payout, sustainable growth, and DDM value. (NUMERICAL)

**Problem.** EPS₁ = ₹25, ROE = 16%, cost of equity r = 11%. The firm pays out 50%. (a) Find g, D₁, and price. (b) If it raised payout to 80%, what happens to value, and why?

**Solution.**
(a) b = 1 − 0.50 = 0.50. g = 0.50 × 16% = **8%**. D₁ = 25 × 0.50 = **₹12.50**.
P₀ = 12.50 / (0.11 − 0.08) = 12.50 / 0.03 = **₹416.67.**

(b) b = 0.20, g = 0.20 × 16% = 3.2%. D₁ = 25 × 0.80 = ₹20.
P₀ = 20 / (0.11 − 0.032) = 20 / 0.078 = **₹256.41.**
Value **falls** (₹416.67 → ₹256.41). **Why:** ROE 16% > r 11%, so reinvestment creates value; paying out more forfeits that spread. Retain more, not less.

---

### Q15. The MM pivot — when payout is irrelevant. (NUMERICAL)

**Problem.** EPS₁ = ₹25, r = 11%, but now **ROE = 11%** (equal to r). Compare payout 50% vs 80%.

**Solution.**
50%: g = 0.5 × 11% = 5.5%; D₁ = 12.50; P = 12.50/(0.11−0.055) = 12.50/0.055 = **₹227.27.**
80%: g = 0.2 × 11% = 2.2%; D₁ = 20; P = 20/(0.11−0.022) = 20/0.088 = **₹227.27.**
**Identical.** When ROE = r, payout is **irrelevant** — MM proven inside the DDM. The value pivot: ROE > r retain, ROE < r pay out, ROE = r indifferent.

---

### Q16. Dividend vs buyback — wealth, EPS, price (tax-free). (NUMERICAL)

**Problem.** 20m shares at ₹50 (cap ₹1,000m), net income ₹120m (EPS ₹6), ₹100m to return. Compare a ₹100m dividend vs a ₹100m buyback at ₹50. Ignore taxes.

**Solution.**
**Dividend:** DPS = 100/20 = ₹5. Ex-price ≈ 50 − 5 = ₹45. Holder of 100 shares: 100×45 + 100×5 = ₹4,500 + ₹500 = **₹5,000.** Shares 20m, EPS unchanged = **₹6.**
**Buyback:** shares bought = 100m/50 = 2m. New count = 18m. Cap after = 1,000 − 100 = ₹900m; price = 900/18 = **₹50** (unchanged). EPS = 120/18 = **₹6.67** (+11%). Non-seller with 100 shares: 100×50 = **₹5,000** and a larger ownership %.
**Conclusion:** total wealth ₹5,000 either way (MM). Buyback raised EPS (₹6 → ₹6.67) but that's the same pie / fewer slices — not new value. Dividend cut price to ₹45; buyback held ₹50.

---

### Q17. Buyback with taxes — the after-tax advantage. (NUMERICAL)

**Problem.** Using Q16, the marginal holder wants cash, faces a 25% dividend tax and 12% capital-gains tax, with cost basis ≈ current price (negligible gain). Which route leaves more after-tax cash for the same ₹500 gross?

**Solution.**
**Dividend:** ₹500 gross × (1 − 0.25) = **₹375 net cash** (+ ₹4,500 stock = ₹4,875).
**Buyback:** sell 10 shares (5% of 100) × ₹50 = ₹500; gain ≈ 0 → tax ≈ 0 → **≈ ₹500 net cash** (+ ₹4,500 stock = ₹5,000).
The buyback leaves **~₹125 more after tax** and lets the investor **choose when** to realize gains. Core tax case for buybacks.

---

### Q18. Residual dividend policy. (NUMERICAL)

**Problem.** Net income ₹200m. Target structure 45% debt / 55% equity. Capital budget ₹300m. Strict residual policy. Find the dividend and payout ratio. Then redo with a ₹400m capital budget.

**Solution.**
Equity portion = 55% × 300 = ₹165m (debt funds ₹135m). Fund from earnings → retain ₹165m. Residual dividend = 200 − 165 = **₹35m.** Payout = 35/200 = **17.5%.**
With ₹400m budget: equity portion = 55% × 400 = ₹220m > ₹200m NI → **dividend = ₹0** and the firm raises ₹20m external equity. Payout = **0%.**
**Point:** same earnings, dividend swings 17.5% → 0% purely on investment needs — why pure residual gives erratic dividends and firms smooth instead.

---

### Q19. Lintner partial adjustment. (NUMERICAL)

**Problem.** Prior DPS ₹9.00. EPS this year ₹28, target payout 55%, speed of adjustment 0.35. Find this year's DPS.

**Solution.**
Target DPS = 55% × 28 = ₹15.40. ΔD = 0.35 × (15.40 − 9.00) = 0.35 × 6.40 = **₹2.24.**
New DPS = 9.00 + 2.24 = **₹11.24.**
The firm moves only 35% toward the ₹15.40 target (not straight to it) to protect against having to cut if earnings dip.

---

### Q20. EPS accretion/dilution of a debt-funded buyback. (NUMERICAL)

**Problem.** Firm: 100m shares, EPS ₹5 (NI ₹500m), share price ₹80 (P/E 16×, earnings yield 6.25%). It borrows ₹800m at 8% pre-tax to buy back 10m shares at ₹80. Tax rate 25%. Is it EPS accretive?

**Solution.**
Shares bought = 800m/80 = 10m → new count = 90m.
After-tax interest cost = 800m × 8% × (1 − 0.25) = 800 × 0.06 = ₹48m.
New NI = 500 − 48 = ₹452m. New EPS = 452 / 90 = **₹5.02** (+0.4%). **Marginally accretive.**
**Check via the rule:** after-tax cost of debt = 8% × 0.75 = 6.0% < earnings yield 6.25% → accretive, but barely. Had the after-tax cost exceeded 6.25% (e.g., 9% pre-tax → 6.75% after-tax), it would be **dilutive.** Illustrates: buybacks are not automatically EPS-positive.

---

### Q21. Total payout ratio with net buybacks. (NUMERICAL)

**Problem.** Net income ₹600m. Dividends ₹150m. Gross buybacks ₹300m, but ₹120m of new stock issued to employees. Find the plain dividend payout, the gross total payout, and the **net** total payout.

**Solution.**
Dividend payout = 150/600 = **25%.**
Gross total payout = (150 + 300)/600 = 450/600 = **75%.**
Net buybacks = 300 − 120 = ₹180m. Net total payout = (150 + 180)/600 = 330/600 = **55%.**
**Lesson:** ignoring buybacks understates cash returned (25% vs 55–75%); ignoring issuance overstates it (75% vs 55%). Always specify gross vs net.

---

### Q22. Ex-dividend price and homemade dividend. (NUMERICAL)

**Problem.** Stock ₹200 cum-dividend, about to pay ₹8 DPS. Ignore taxes. (a) Ex-date price? (b) An investor holding 50 shares wants ₹1,000 of cash but the firm paid nothing — how do they replicate it, and is their wealth the same?

**Solution.**
(a) Ex-price ≈ 200 − 8 = **₹192.**
(b) With the ₹8 dividend: 50 shares → ₹400 cash + 50×192 = ₹9,600 stock = **₹10,000**, but that's only ₹400 cash (short of ₹1,000). To get ₹1,000 with no dividend: at ₹200, sell 5 shares = ₹1,000 cash; keep 45 shares × ₹200 = ₹9,000. Total = **₹10,000.** Same total wealth — a **homemade dividend** exactly replicates the payout (tax-free). Taxes/transaction costs are what make the real choice matter.

---

## One-line answer key (self-check)

| Q | Key result |
|---|---|
| 14 | g=8%, D₁=₹12.50, P=₹416.67; higher payout → ₹256.41 (falls, ROE>r) |
| 15 | Both ₹227.27 — payout irrelevant when ROE=r |
| 16 | Wealth ₹5,000 both; buyback EPS ₹6→₹6.67, price stays ₹50 |
| 17 | Dividend ₹375 net vs buyback ~₹500 net — buyback +₹125 |
| 18 | Dividend ₹35m (17.5%); with ₹400m budget → ₹0 (0%) |
| 19 | New DPS ₹11.24 (moved ₹2.24 of ₹6.40 gap) |
| 20 | EPS ₹5.00→₹5.02, barely accretive (6.0% < 6.25%) |
| 21 | Payout 25%; gross total 75%; net total 55% |
| 22 | Ex-price ₹192; homemade dividend replicates, wealth ₹10,000 |
