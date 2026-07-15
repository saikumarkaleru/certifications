# SEBI, Regulation & Staying Safe

## Why this matters — the pro vs retail gap this closes

The Indian retail trader loses money two ways: to the market, and to the ecosystem of people who prey on retail traders. Telegram "sure-shot" tip channels, fake "SEBI-registered" advisors, unregistered PMS pitches promising 10%/month, and copy-trading scams strip more wealth from beginners than any bad chart pattern. Meanwhile, honest ignorance of the rules — trading on a friend's tip that turns out to be insider information, or running a banned open-API algo — can land a trader in a SEBI enforcement action. A professional knows exactly **what retail is allowed to do, who is legally permitted to advise them, and how to spot a scam in ten seconds**. This chapter is your legal and safety perimeter.

*(All rules current as of 2026; verify on sebi.gov.in, NSE/BSE circulars, and the SCORES portal — regulations change.)*

## The essentials — the rules that protect you

**What retail is allowed.** You can trade cash equity, F&O (index, stock, currency, commodity), ETFs, bonds — through a **SEBI-registered broker** with a demat at **NSDL or CDSL**. You may use your broker's tools and *registered* APIs. You may **not**: use banned open APIs for algos, take positions on **UPSI** (unpublished price-sensitive information), or run an unregistered advisory/PMS for others.

**The 2026 retail algo framework (mandatory from 01-Apr-2026).** SEBI now regulates retail algorithmic trading:
- Every algo order must carry an **exchange-issued Algo-ID** (tagged and traceable).
- **Open/unauthenticated APIs are banned.** Retail algos run **only via a registered broker's API with proper authentication**.
- Orders above **10 orders/second** need exchange approval/registration.
- The **broker is responsible** for algos on its platform; **third-party algo vendors must tie up with a registered broker** and register the strategy.
- Practical effect: the era of plugging a random GitHub bot into an open API is over. If a vendor offers you an "unlimited open-API algo," it is now **illegal** — walk away.

**Insider trading & UPSI (SEBI PIT Regulations, 2015 as amended).** Trading on unpublished price-sensitive information — a results leak, an unannounced merger, a tip from someone inside the company — is a **criminal offence** with disgorgement, heavy penalties, and bans. This includes acting on a WhatsApp forward of "results before announcement." If information isn't public, you cannot trade on it.

**Who may legally advise you.** Only two categories:
- **SEBI Registered Investment Adviser (RIA)** — can give personalised advice for a fee; must disclose registration number, act as a fiduciary.
- **SEBI Registered Research Analyst (RA)** — can issue research/recommendations with disclosures.
Anyone else giving buy/sell calls for money — Telegram admins, YouTubers running paid groups, "PMS" operators below the ₹50 lakh regulated threshold — is **operating illegally**. Verify any adviser on the **SEBI RIA/RA public list** by their registration number.

**Portfolio Management Services (PMS)** is legitimate but has a **₹50 lakh minimum** and must be SEBI-registered. Anyone pooling smaller amounts "as a PMS" is running an unregistered scheme — a scam.

## Worked example — spotting the scam in real time

Arjun gets a Telegram invite: *"SEBI-certified Bank Nifty experts — 90% accuracy, ₹5,000/month, join VIP for jackpot calls. Send screenshots of profit for testimonials."* He does three checks:

1. **Registration:** The channel claims "SEBI-certified." Arjun searches the **SEBI RA/RIA list** for the name/number. Not found. → *Red flag: no registration; "certified" is meaningless — only "registered" counts.*
2. **Claim:** "90% accuracy, jackpot calls." SEBI **bars registered advisers from promising assured/guaranteed returns.** A real RA never advertises accuracy percentages or "jackpots." → *Red flag.*
3. **Model:** Pay a subscription, get calls in a group, no risk disclosure, no fiduciary duty, testimonials harvested to recruit more. Classic **tip-seller pump**: admins often hold positions and dump on followers. → *Red flag.*

Arjun leaves. Contrast: a genuine RIA gives him a signed agreement, a registration number he verifies on sebi.gov.in, risk profiling, fee transparency, and **never** guarantees returns. Cost of the lesson if he'd stayed: subscription fees plus losses on pumped calls, which SEBI studies repeatedly show run into the tens of thousands per victim.

## How pros do it / common mistakes

**How pros do it**
- **Verify every adviser** against the SEBI RA/RIA list before paying a rupee; keep the registration number on file.
- Treat any **guaranteed-return / fixed-% monthly** pitch as automatically fraudulent — SEBI prohibits it, and markets can't deliver it.
- Use **only registered broker APIs** for automation, with a proper Algo-ID; never touch an "open API" workaround post-01-Apr-2026.
- **Never trade on non-public information**, however tempting — the legal downside dwarfs any gain.
- Keep records and know the **SCORES** grievance route.

**Common mistakes / red flags**
- Joining paid Telegram/WhatsApp "tip" groups and copy-trading strangers.
- Believing "SEBI-certified/approved" — SEBI **registers**, it never "approves" or "certifies" tipsters or returns.
- Handing money to an unregistered "PMS" or "fund manager" pooling small tickets.
- Acting on leaked results / insider tips.
- Running or buying banned open-API algo bots.

**Ten-second red-flag scan:** guaranteed/assured returns • accuracy % or "jackpot" claims • urgency ("last 2 seats") • pay-to-join calls with no registration number • profit-screenshot marketing • asking you to trade in *their* account or share login. Any one = walk away.

## Checklist / drill — stay-safe checklist

- [ ] Adviser has a **verifiable SEBI RIA or RA registration number** (checked on sebi.gov.in).
- [ ] No **guaranteed / assured / fixed-%** return promise anywhere.
- [ ] No **accuracy-%, "jackpot," or urgency** marketing.
- [ ] PMS pitch: SEBI-registered **and** ≥ ₹50 lakh minimum — else refuse.
- [ ] Automation only via **registered broker API with Algo-ID**; no open APIs.
- [ ] You are **not** trading on any non-public / insider information.
- [ ] You never share broker login or trade in someone else's account.
- [ ] You know how to file a complaint on **SCORES** (scores.sebi.gov.in).

**Grievance path:** first raise with the broker/adviser in writing; if unresolved in ~30 days, escalate on **SCORES** (SEBI's complaint portal); disputes with brokers can also go to **exchange investor grievance / arbitration**. Keep contract notes and communications as evidence.

**Drill:** Take the last three "tips" or advisory pitches you've seen (Telegram, YouTube, a friend). Run each through the ten-second red-flag scan and try to find a real SEBI registration number. You will likely find **zero** are registered — proof of how much of the retail information diet is unregulated noise or outright fraud. *Verify all of the above on SEBI/NSE/BSE — 2026 rules change.*
