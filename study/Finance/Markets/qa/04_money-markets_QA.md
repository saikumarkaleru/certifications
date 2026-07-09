# Q&A — Money Markets and Instruments

A companion practice bank for Chapter 04. Every question is followed by a full answer. Work each one before reading the answer; the goal is understanding, not recognition.

---

## Section A — Concept-Check Questions

**A1. In one sentence, what is the money market, and what single dividing line separates it from the capital market?**

The money market is the wholesale market for debt with an **original maturity of one year or less**. The only dividing line from the capital market is **original maturity**: at or below one year is money market, above one year is capital market. The test is original maturity, not residual — a 10-year bond with three months left to run is *not* a money-market instrument.

**A2. Name the three defining traits every money-market instrument inherits, and explain why they cluster together.**

(1) **Short maturity** (overnight to one year), which keeps interest-rate risk tiny and returns cash quickly. (2) **High safety and liquidity** ("near-money"), because participants are parking cash they must get back intact. (3) **Low, wholesale returns in large denominations**, because safe-and-short assets pay little and the market is institutional. They cluster because they all flow from the same purpose — short-term liquidity management — which demands you sacrifice yield for safety and instant retrievability.

**A3. What is a "discount instrument," and how does an investor earn a return on one?**

A discount instrument pays no periodic coupon. It is sold **below** face value and redeemed **at** face value; the investor's return is the difference (the discount). Buy a 91-day T-bill of face ₹100 for ₹98.30 today, receive ₹100 in 91 days — the ₹1.70 is the income.

**A4. Distinguish bank discount yield from bond-equivalent yield (BEY). Which is higher, and why?**

Bank discount yield measures the discount against **face value** using a **360-day** year: (Face − Price)/Face × 360/days. BEY measures it against the **price actually paid** using a **365-day** year: (Face − Price)/Price × 365/days. **BEY is always higher** because it divides by the smaller number (price < face) and multiplies by more days (365 > 360). BEY is the economically honest return because you invested the price, not the face.

**A5. List the five core Indian money-market instruments and state whether each is secured or unsecured.**

Treasury bills (sovereign, effectively zero credit risk — unsecured but risk-free); Commercial Paper (**unsecured** corporate promissory note); Certificate of Deposit (**unsecured**, bank-issued, but negotiable); Call/Notice/Term money (**unsecured** interbank); Repo/Reverse Repo (**secured/collateralised** by government securities).

**A6. Why is the central bank described as the "anchor" of the money market?**

Because all payments ultimately settle across banks' reserve accounts at the central bank, the pool of cash the money market trades is fundamentally **central-bank reserves**. By injecting or draining reserves, the central bank moves the overnight rate, which cascades up the maturity curve into every other money-market instrument. This makes the money market the **transmission belt of monetary policy** and the first place a policy-rate change bites.

**A7. What is the difference between a CD and an ordinary fixed deposit?**

A CD is **negotiable/transferable** — the holder can sell it in the secondary market before maturity, which is why it qualifies as a money-market instrument. A fixed deposit is a **non-transferable bilateral contract** with a premature-withdrawal penalty. They feel similar, but only the CD trades.

**A8. Define rollover risk and name one instrument most exposed to it.**

Rollover (refinancing) risk is the risk of being **unable to refinance maturing short-term debt**. **Commercial Paper** is the classic case: it is short and must be constantly rolled, so if confidence in the issuer evaporates it cannot be reissued — the mechanism behind the IL&FS (2018) and 2008 US CP freezes.

**A9. Order the three rungs of the RBI's LAF corridor from lowest to highest rate, and state what each does.**

**SDF (floor)** — the rate at which the RBI absorbs surplus liquidity from banks, without giving collateral. **Repo rate (policy anchor, middle)** — the rate at which the RBI lends overnight to banks against G-secs. **MSF (ceiling)** — the emergency rate at which banks can borrow overnight above repo against SLR securities. The RBI steers the weighted-average call rate to hug the repo rate inside this corridor.

**A10. True or false: "Reverse repo injects liquidity into the banking system." Correct if false.**

False. From the RBI's operations, **repo injects** cash into banks (RBI lends), while **reverse repo / SDF absorbs** cash from banks (RBI borrows). Memorise the *direction of cash*, not the label.

---

## Section B — Applied / Scenario Questions

**B1. The RBI auctions a 182-day T-bill, face ₹100, cut-off price ₹96.60. Compute the bond-equivalent yield (365-day basis).**

Discount income = 100 − 96.60 = ₹3.40 on ₹96.60 invested for 182 days.
BEY = (3.40 / 96.60) × (365 / 182) = 0.03520 × 2.0055 = **7.06% p.a.**
So a treasurer buying at ₹96.60 earns roughly 7.06% annualised on money actually deployed.

**B2. A AAA manufacturer needs ₹200 crore for 90 days. A bank cash-credit line costs 8.6% p.a.; 90-day CP prices at 7.5% p.a. plus 0.15% annualised issuance costs. Which is cheaper, by how much, and what is the catch?**

Bank loan: 200 × 8.6% × 90/365 = **₹4.24 crore.**
CP all-in 7.65%: 200 × 7.65% × 90/365 = **₹3.77 crore.**
CP saves roughly **₹47 lakh** for one cycle — disintermediation, capturing the bank's margin. The catch is **rollover risk**: if the firm keeps rolling CP and its rating slips or markets seize, it may be unable to refinance. Prudent treasuries therefore keep **committed backup bank lines** behind the CP programme.

**B3. Bank X is ₹800 crore short of its required RBI reserves at day-end. It borrows overnight via LAF repo at 6.50%. What does the transaction look like mechanically, and what interest does it pay?**

Bank X **sells ₹800 crore (market value) of G-secs to the RBI** overnight, receives cash (after a small haircut), and agrees to buy them back the next morning at a higher price reflecting 6.50%. Overnight interest ≈ 800 × 6.50% × 1/365 ≈ **₹14.2 lakh.** Next morning the leg reverses: Bank X repays cash plus interest and takes back its bonds. Economically it is a collateralised loan, not a sale.

**B4. A liquid mutual fund has ₹500 crore of surplus for one night. It cannot lend in the call market. How does it deploy the cash, and why is this route open to it?**

It lends through **TREPS (Triparty Repo)** operated by CCIL, or buys T-bills / short CP / CDs. TREPS is open to it because a third party (the clearing corporation) manages collateral and settlement, making it safe for a wide participant set including mutual funds and insurers. The **call money market is interbank-only** (banks and primary dealers), so corporates and mutual funds access the money market via repo/TREPS and liquid instruments, never call money.

**B5. Rates rise sharply the week after an investor buys a 364-day T-bill, and she needs to sell it early. Is she guaranteed to get face value? Reconcile this with "T-bills are risk-free."**

No. Held to maturity a T-bill is risk-free — she will receive ₹100. But **sold early into a market where rates have jumped, its price will have fallen** slightly, so she may realise less than expected. "Risk-free" refers to **default risk and hold-to-maturity**, not intraday **price risk**. Credit risk is essentially zero; price risk on early sale is not.

**B6. During a confidence shock, an NBFC that funded 5-year infrastructure loans with 90-day CP suddenly cannot roll its paper. Explain the failure and the underlying structural error.**

The NBFC has an **asset-liability mismatch**: long, illiquid assets financed with short, unstable liabilities. As long as CP rolls smoothly it works, but the moment lenders lose confidence (e.g., a rating downgrade or a sector-wide scare like IL&FS 2018), the CP market freezes and the NBFC cannot refinance maturing paper while its cash is locked in multi-year loans. The result is a liquidity crunch that can turn a solvent firm insolvent. The structural error is funding long assets with short money — the core lesson that reshaped RBI/SEBI treatment of ALM and liquid-fund holdings.

**B7. A treasurer must choose between a 91-day T-bill yielding 6.9% (BEY) and 91-day AAA CP yielding 7.6%. What explains the 0.7% gap, and what should drive the choice?**

The gap is a **credit spread**. The T-bill carries the sovereign's effectively zero credit risk; the CP is **unsecured corporate credit**, so investors demand extra yield to compensate for default and liquidity risk. The choice should turn on the treasurer's mandate: for a cash-equivalent bucket that must be pristine, the T-bill's safety and superior liquidity justify giving up 0.7%; if the mandate permits taking measured AAA credit risk for extra return, the CP is defensible — but only with an eye on issuer concentration and rollover conditions.

---

## Section C — Interview-Style Questions

**C1. "Walk me through what a repo actually is, and why banks prefer it to call money."**

A repo is the sale of a security — typically a government bond — with a simultaneous agreement to buy it back at a fixed higher price on a future date. Economically it is a **collateralised loan**: the seller borrows cash, the buyer lends cash and holds the bond as collateral, and the price difference is the interest. It is called a repo from the borrower's side and a reverse repo from the lender's side — one transaction, two names. Banks prefer it to unsecured call money because it is **secured**: if the borrower defaults, the lender keeps the government bond, protected further by a **haircut** (lending slightly less than the collateral's market value). That safety is why repo — in India largely via **TREPS** — has displaced unsecured call money as the dominant overnight market.

**C2. "What is the difference between discount yield and bond-equivalent yield, and which would you quote a client?"**

Discount yield measures the discount as a fraction of **face value** on a **360-day** year; bond-equivalent yield measures it as a fraction of the **price actually paid** on a **365-day** year. BEY is always higher and is the **economically correct** number, because it reflects the return on money you truly invested (the price) over the true calendar year. I would quote the client the **BEY** — quoting the discount yield understates the real return and, in an interview, mistaking one for the other signals you don't understand discount instruments.

**C3. "How does a change in the RBI's repo rate reach the real economy?"**

Through the **monetary-policy transmission chain**, starting in the money market. The RBI changes the repo rate, which moves the **weighted-average call rate / MIBOR** as the overnight market re-prices inside the LAF corridor. That overnight move ripples up the short curve into **T-bill, CP, and CD rates**. Banks then reset lending rates through the **external benchmark / MCLR** framework, and finally borrowing costs for households and firms change, affecting spending and investment. The money market is the **first link** — which is exactly why central banks obsess over keeping the overnight rate pinned near the policy rate.

**C4. "Why do only the strongest companies issue commercial paper?"**

Because CP is **unsecured** — it is backed by nothing but the issuer's own creditworthiness, with no collateral behind it. Investors will buy it only from names they trust to repay, so regulation reinforces this with a **minimum credit rating** (A3 or better in India), a sanctioned working-capital limit, and standard-asset classification. The appeal for a top-rated issuer is cost: CP is **cheaper than a bank cash-credit loan** because it cuts out the bank's intermediation margin. But its safety rests entirely on **credit quality and the ability to roll over** — a downgrade or a market freeze can inflict real losses, as IL&FS and DHFL showed.

**C5. "The RBI does a repo — is it injecting or draining liquidity? Many candidates get this backwards."**

When the **RBI does a repo, it lends cash to banks against G-secs, so it injects liquidity.** When it does a **reverse repo (or absorbs via the SDF), it takes cash from banks, so it drains liquidity.** The confusion comes from arguing over labels; the reliable rule is to track **who gets the cash and who holds the bond**. RBI repo → cash goes to banks → injection. One caveat worth flagging: since April 2022 the **SDF replaced the fixed reverse repo** as India's effective corridor floor, so calling the "reverse repo rate" the floor is outdated.

**C6. "If T-bills are risk-free, why does anyone hold anything else in a cash portfolio?"**

Because "risk-free" means free of **default** risk when **held to maturity** — it does not mean the highest return or the only sensible holding. T-bills pay the lowest yield precisely because they are the safest; a treasurer willing to accept a sliver of AAA credit risk can pick up extra yield in CP, CDs, or TREPS while staying liquid. A well-run cash book also diversifies across instruments and maturities to match its own liquidity ladder and to avoid concentration, even in sovereign paper. So the choice is a deliberate trade along the **risk-return-liquidity triangle**, not a failure to notice T-bills exist.

**C7. "Give me the one-sentence framing of what the money market is."**

The money market is where the economy's short-term cash is safely and instantly reallocated from surplus holders to deficit holders, priced off the central bank's overnight rate — the **risk-free short end of the yield curve.**

---

## Section D — Multiple-Choice Questions (with reasoning)

**D1. Which instrument is a collateralised (secured) money-market transaction?**
(a) Commercial Paper (b) Certificate of Deposit (c) Repo (d) Call money

**Answer: (c) Repo.** A repo is backed by government-security collateral, protected by a haircut. CP, CDs, and call money are all **unsecured**, relying on the issuer's or counterparty's credit.

**D2. A 91-day T-bill is bought at ₹98.50 (face ₹100). Its bond-equivalent yield (365-day basis) is closest to:**
(a) 6.02% (b) 6.11% (c) 5.94% (d) 6.20%

**Answer: (b) 6.11%.** BEY = (1.50 / 98.50) × (365 / 91) = 0.01523 × 4.0110 = 6.11%. Dividing by face (₹100) instead would give the lower discount yield (~6.01%), the classic trap.

**D3. In India, participation in the call money market is restricted to:**
(a) All corporates and banks (b) Banks and primary dealers only (c) Mutual funds and banks (d) Anyone via demat account

**Answer: (b) Banks and primary dealers only.** Call money is a pure interbank market for meeting daily reserve needs. Corporates and mutual funds access the money market through repo/TREPS and liquid funds instead.

**D4. Which correctly describes the RBI's LAF corridor from floor to ceiling?**
(a) Repo < SDF < MSF (b) SDF < Repo < MSF (c) MSF < Repo < SDF (d) SDF < MSF < Repo

**Answer: (b) SDF < Repo < MSF.** SDF is the absorption floor, the repo rate is the policy anchor in the middle, and MSF is the emergency-lending ceiling.

**D5. The 2018 IL&FS episode is most directly an illustration of:**
(a) Interest-rate risk on T-bills (b) Currency mismatch (c) Rollover / refinancing risk on short-term debt (d) Equity market volatility

**Answer: (c) Rollover / refinancing risk.** IL&FS defaulted on short-term paper it could no longer refinance, hitting liquid funds and NBFCs that had funded long assets with short CP. It is the textbook case of short-term debt becoming a rollover trap when confidence breaks.

**D6. A 5-year corporate bond has 4 months left until maturity. It is:**
(a) A money-market instrument, because residual maturity is under a year (b) A capital-market instrument, because original maturity exceeded a year (c) Reclassified as CP (d) A T-bill equivalent

**Answer: (b) A capital-market instrument.** The classification test is **original** maturity, not residual. Having under a year left does not convert a bond into a money-market instrument.

**D7. Why is the bond-equivalent yield always higher than the bank discount yield for the same T-bill?**
(a) It uses a 360-day year (b) It divides by face value (c) It divides by the (smaller) price and uses 365 days (d) It includes a coupon

**Answer: (c).** BEY divides the discount by the price actually paid (smaller than face) and annualises over 365 rather than 360 days — both adjustments push the number up. There is no coupon on a discount instrument.

**D8. When the RBI conducts a reverse repo / SDF operation, it is:**
(a) Injecting durable liquidity (b) Lending to banks against collateral (c) Absorbing surplus liquidity from banks (d) Buying bonds outright

**Answer: (c) Absorbing surplus liquidity.** In a reverse repo / SDF, banks park cash with the RBI, so liquidity is drained from the system. Outright bond buying would be an OMO; lending to banks would be a repo.

---

*End of Q&A bank — Chapter 04, Money Markets and Instruments.*
