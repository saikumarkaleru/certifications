# Case Study: Expiry-Day Option Behaviour & Theta Crush

*Price levels here are approximate reconstructions of real weekly-expiry sessions; pull up the actual chart to verify the exact ticks — the transferable value is the mechanics of how premium decays and pins, not the precise numbers.*

Expiry day is the one session where time itself is the dominant force. On a normal trading day, an option's price moves mostly with the underlying (delta) and with fear (vega). On the last day of a weekly contract, both of those fade and the third Greek — theta, time decay — takes over. By the close, every out-of-the-money option is worth exactly zero, no matter how loudly it was quoted at 9:20 a.m. The two case studies below walk a real Nifty weekly expiry and a real Bank Nifty weekly expiry, hour by hour, so you can see who gets paid and who gets zeroed.

## Case A — A "pin day" Nifty weekly expiry (a quiet Thursday)

**The setup.** A mid-week Nifty weekly expiry, Nifty opened around 22,050 after a flat global session. No major event on the calendar — no RBI, no US CPI, no results heavyweight. This is the most common kind of expiry: a range-bound drift day. Nifty lot size 75 (post-2024 revision). The interesting question wasn't direction; it was *how fast the OTM premiums would bleed*.

**Price-action walkthrough.** Watch the 22,100 call (roughly 50 points OTM at open) and the 22,000 put.

| Time | Nifty spot | 22,100 CE | 22,000 PE | What happened |
|------|-----------|-----------|-----------|----------------|
| 9:20 | 22,050 | ~48 | ~46 | Both OTM strikes still carry full "hope" premium |
| 10:30 | 22,070 | ~40 | ~34 | Spot barely moved; both premiums leaking |
| 12:00 | 22,040 | ~26 | ~30 | Lunch-hour lull — theta accelerating, IV falling |
| 13:30 | 22,060 | ~15 | ~14 | Premium now almost pure time value, thinning fast |
| 14:30 | 22,055 | ~7 | ~6 | Market "pinning" near 22,050 — max-pain magnet |
| 15:15 | 22,048 | ~1 | ~2 | Last 15 min: both racing to zero |
| 15:30 | 22,045 | 0 | 0 | Both expire worthless |

Notice the shape: the decay is not linear. From 12:00 to 15:30, the 22,100 CE fell from 26 to 0 — most of the loss came in the back half of the day. That is theta acceleration: on expiry day, time value collapses on a curve, steepest into the close.

**The trade.** A theta seller sold the 22,100 CE and the 22,000 PE at 10:30 — a short strangle — collecting roughly 40 + 34 = 74 points. One lot each: 74 × 75 = ₹5,550 credit. Margin for a two-legged short strangle ran roughly ₹1.4–1.6 lakh. Stop plan: exit a leg if Nifty closed decisively through 22,150 or 21,950 (the short strikes).

**What happened.** Nifty never threatened either strike. By 15:15 both legs were near zero and the seller let them expire. Gross profit ≈ ₹5,550. Costs on expiry are real and disproportionately large because you're trading cheap premium: STT on options is charged on premium for normal sells, but on *exercised/settled* ITM options STT is charged on intrinsic value — a trap we'll revisit. Here both expired OTM (worthless), so no exercise STT. Brokerage + exchange fees + GST on two legs ≈ ₹120–150. Net ≈ ₹5,400 on ₹1.5 lakh margin for one day — a clean theta harvest.

**The lesson.** The seller got paid for doing nothing while the buyer of those same options paid full price at 10:30 and watched it evaporate. On a pin day, the max-pain level (the strike where the most option premium expires worthless) acts like a magnet, and market-maker hedging tends to reinforce it. The retail mistake: buying cheap OTM options at lunchtime "because they're only ₹15" — that ₹15 is ₹15 of pure decay with a strong statistical bias to zero.

## Case B — A Bank Nifty expiry that bit the sellers (the last-hour gamma spike)

**The setup.** A Bank Nifty weekly expiry, index opened near 48,200. Quiet until 14:00, then a sharp move (a heavyweight private bank ripped on a block deal / sector news). Bank Nifty lot size 30. This is the tail that keeps expiry sellers honest.

**Price-action walkthrough.** Watch the 48,300 CE, which looked "safely OTM" all morning.

| Time | Bank Nifty | 48,300 CE | What happened |
|------|-----------|-----------|----------------|
| 9:30 | 48,200 | ~90 | OTM, decaying normally |
| 12:00 | 48,180 | ~45 | Looks dead — sellers relaxed |
| 14:00 | 48,250 | ~55 | Sudden bid, spot creeping up |
| 14:45 | 48,480 | ~230 | Breakout — CE now deep ITM, premium exploded |
| 15:15 | 48,560 | ~275 | Gamma move: a 45→275 round trip in 75 min |
| 15:30 | 48,540 | ~240 (settles to intrinsic) | Expires ITM by ~240 |

That is the gamma bomb. Near expiry, an at-the-money option's delta flips from near-0 to near-1 over a tiny range of spot — so a modest index move detonates the premium. The 48,300 CE went from a decaying ₹45 to ~₹240 intrinsic, a 5x, in the final ninety minutes.

**The trade (from the seller's side).** A seller had shorted that 48,300 CE at 12:00 for 45 — one lot, credit 45 × 30 = ₹1,350. Felt free. Stop discipline said: cover if Bank Nifty prints 48,300. It hit 48,300 around 14:30; a disciplined seller covered near a premium of ~120, losing (120 − 45) × 30 = ₹2,250. The seller who *didn't* honour the stop — "it's expiry, it'll come back" — held into 15:15 and covered near 250, losing (250 − 45) × 30 = ₹6,150. Plus the sting: an ITM option left to expire attracts STT on the full intrinsic value, so letting it settle is often worse than covering.

**What happened.** One afternoon erased what several quiet pin-day expiries had earned. The buyer of that 48,300 CE — probably dismissed all morning as a gambler — made the 5x.

**The lesson.** Theta selling on expiry has a beautiful equity curve most weeks and a cliff a few weeks a year. The professional sizes for the cliff and covers at the stop mechanically. The retail seller treats the quiet weeks as proof of safety, sizes up, skips the stop, and hands back a quarter's income in one gamma spike.

## Transferable rules

- **Expiry decay is a curve, not a line** — the steepest theta bleed is in the last two hours, so late-day OTM buying is buying almost-pure decay.
- **Sellers are structurally favoured on pin days**, but you are collecting small premium against a fat tail — always define the tail and size the position for it, not for the average week.
- **Respect the gamma flip near your short strike** — set a hard stop at the strike and cover mechanically; "it's expiry, it'll come back" is how sellers blow up.
- **Never let a short ITM option expire to settlement** — STT on exercised options is charged on intrinsic value, so squaring off is usually cheaper than getting assigned.
- **Max-pain is a tendency, not a guarantee** — it works until real news arrives, and it never protects you on an event day, so trade smaller (or not at all) when the calendar is hot.
