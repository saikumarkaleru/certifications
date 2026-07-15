# Clearing, Settlement & Depositories

## Why this matters

Retail traders think a trade ends the moment the order fills. It doesn't — it ends two business days later when money and shares actually change hands through a clearing corporation and a depository. Not understanding this plumbing is why traders get blindsided by **short-delivery auctions** (you sold shares you didn't have and got penalised), by **DP charges** appearing on sells, by **T+1 funds** not being withdrawable immediately, and by **POA/DDPI** authorisations they signed without reading. Pros understand settlement because it governs *when* they can redeploy capital, *why* certain BTST trades carry auction risk, and *how* their shares are actually held and pledged. This chapter is the market's back-office — invisible until it costs you.

## The essentials

**Rolling settlement — T+1 (as of 2026).** Indian equities settle on a **T+1 rolling** basis: a trade done on Trade day (T) settles the **next business day**. Buyer's demat is credited and seller's bank is credited on T+1. India was the first major market to move fully to T+1 (completed Jan 2023). **T+0 (same-day) settlement** is live as an **optional beta** for a growing list of select stocks — you can opt in for same-day pay-in/pay-out; it runs alongside T+1, not replacing it. *(Status as of July 2026 — verify the current T+0 stock list and rollout on NSE/SEBI; it is expanding.)*

**Clearing corporations.** Between buyer and seller sits a **Clearing Corporation** that becomes the central counterparty (CCP) and guarantees settlement — you never face counterparty default risk directly. On NSE it is **NSE Clearing Ltd (NSCCL / NSE Clearing)**; on BSE it is **Indian Clearing Corporation Ltd (ICCL)**. They net obligations, collect margins, run the settlement guarantee fund, and manage the auction for short deliveries.

**Depositories & DPs.** Shares are held electronically (dematerialised) at one of two depositories — **NSDL** and **CDSL**. You don't deal with them directly; your broker is a **Depository Participant (DP)** — the interface to the depository. Your demat account lives at NSDL or CDSL via your DP.

**Pay-in / pay-out.** On the settlement day the CCP collects securities and funds (**pay-in**) from those who owe, and distributes (**pay-out**) to those due. For a delivery buy, cash pays in and shares pay out to your demat on T+1.

**Short delivery & auction.** If a seller fails to deliver shares on pay-in (sold intraday-style but couldn't cover, or a demat glitch), it's **short delivery**. The exchange conducts an **auction** to buy those shares in the market and deliver to the buyer; the defaulting seller pays the auction price plus penalty — which can be **well above** the sale price (auction price can be marked up). This is the hidden risk in **BTST** (Buy Today Sell Tomorrow): you sell on T+1 shares that haven't hit your demat yet — if your *purchase* was short-delivered, your sale short-delivers and you eat the auction penalty.

**DP charges.** A flat **DP charge** (typically ~₹13–20 + GST per scrip per day, CDSL/NSDL + broker) applies **on the sell/debit side** of delivery holdings — not on buys, not on intraday, not on F&O. Many traders are surprised to see it.

**POA / DDPI.** To let the broker debit shares from your demat when you sell, you historically signed a **Power of Attorney (POA)**. SEBI replaced this with the narrower **DDPI (Demat Debit and Pledge Instruction)** — it authorises *only* delivery-sell debits and margin pledge, not blanket access. Alternatively you can skip DDPI and authorise each sell via **CDSL TPIN/eDIS OTP**. Prefer DDPI over open-ended POA.

## Worked example — a settlement timeline

You buy **100 shares of Reliance at ₹2,950** delivery on **Monday (T)**:

- **Monday (T):** Order fills. ₹2,95,000 + charges is blocked. Trade sent to NSE Clearing; you have an *obligation*, not yet the shares.
- **Tuesday (T+1):** **Pay-in** — funds debited from your account to the CCP. **Pay-out** — 100 Reliance credited to your **CDSL/NSDL demat** via your DP, usually by evening. Now they're truly yours; you can pledge/withdraw.
- If instead you'd **sold** 100 Reliance held in demat on Monday: shares debited via **DDPI** on T+1 pay-in, **funds credited** to your bank/ledger on T+1 pay-out, minus a **DP charge** of ~₹18 + GST (one scrip, sell side).

**Short-delivery case:** You do **BTST** — buy Monday, sell Tuesday morning. But your Monday buy was **short-delivered** by the counter-party, so on Tuesday your demat is empty and your Tuesday sale can't deliver on Wednesday pay-in. The exchange **auctions** the shares Wednesday; if Reliance gapped up and auction clears at ₹3,050, you pay the **₹100/share difference + penalty** — a loss purely from settlement mechanics, not your view. *(Verify current auction/close-out rules on NSE — they change.)*

## How pros do it / common mistakes

**Pros:**
- Plan capital around **T+1 availability** — funds from a sell are usable per broker's ledger rules; don't assume instant bank withdrawal.
- Treat **BTST as carrying auction risk** and avoid it on illiquid or recently-listed names where short delivery is common.
- Use **DDPI or TPIN**, never a blanket POA; know exactly what they authorised.
- Watch **DP charges** eroding small delivery trades — they make tiny share-count delivery scalps uneconomic.
- Consider **T+0 opt-in** where available to free capital same day.

**Retail mistakes:**
- Assuming a trade "ends" at fill and being shocked by **T+1** fund timing.
- Doing **BTST** blind to **short-delivery/auction** penalties.
- Signing an **open POA** giving broad demat access.
- Ignoring **DP charges** on frequent small delivery sells.
- Not knowing whether their demat is at **NSDL or CDSL** (matters for IPO/transfer/eDIS).

## Checklist / drill

- [ ] I know my instrument's **settlement cycle** (T+1, or T+0 if opted in).
- [ ] For any **BTST**, I've accepted **auction/short-delivery risk**.
- [ ] I authorised sells via **DDPI/TPIN**, not blanket POA.
- [ ] I've accounted for **DP charges** on delivery sells.
- [ ] I know my **CCP (NSE Clearing/ICCL)** and **depository (NSDL/CDSL)**.

**Drill:** Take your last delivery buy and sell. On a timeline, write T, T+1, the exact pay-in/pay-out events, the DP charge on the sell, and when funds were actually withdrawable. Then look up whether any stock you trade is on the **T+0 beta list** and note how opting in would change your capital cycle.
