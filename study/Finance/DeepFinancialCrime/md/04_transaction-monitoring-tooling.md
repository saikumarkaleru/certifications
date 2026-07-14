# Transaction Monitoring & Tooling (Actimize, SAS, Oracle FCCM, Quantexa, Napier)

## What you'll be able to do

Explain how a transaction-monitoring (TM) system turns raw transactions into investigable alerts; name the standard **typologies/scenarios** and the **rules and thresholds** that detect them; know what each major tool is good at; **triage and score an alert**; understand **tuning** and the false-positive problem; and use **network/entity analytics** to see risk a single-account rule misses. You'll work a real alert-triage example to a documented decision — the daily job of a TM investigator.

## The essentials

**What TM does:** ingests transactions (deposits, wires, trades, card activity), runs them against **scenarios** (rules encoding known laundering behaviour), and generates **alerts** when thresholds trip. An analyst triages each alert → close as false positive, or escalate to a **case** → potentially an **STR**.

**Core typologies & the rule that catches them:**

| Typology | Rule logic (illustrative) |
|---|---|
| **Structuring / smurfing** | Multiple cash deposits just under ₹10 lakh / ₹50,000 PAN limit within N days |
| **Rapid movement of funds** | Credit followed by near-total debit within 24–48h ("pass-through"/flow-through) |
| **Round-tripping** | Funds out and back via related parties/jurisdictions |
| **High-risk geography** | Wires to/from FATF grey/black-list countries |
| **Unusual for profile** | Activity ≫ expected turnover declared at KYC (deviation from peer/self baseline) |
| **Dormant-then-active** | Long-inactive account suddenly high-volume |
| **Mule activity** | Many inbound credits from unrelated parties, quick cash-out |
| **Trade-based ML** | Over/under-invoicing, mismatched shipment values |

**Rules vs thresholds vs scenarios:** a **scenario** is the pattern (e.g., "rapid movement"); the **rule** is the codified logic; the **threshold** is the tunable number (amount, count, days, %). Thresholds are calibrated by segment — a corporate treasury and a retail savings account can't share the same limit.

**The tools:**

| Tool | Best at |
|---|---|
| **NICE Actimize** | Market-leading, broad AML suite (SAM for TM, WLF for screening, actone case mgmt); strong out-of-the-box scenarios, widely used in banks/GCCs |
| **SAS AML** | Powerful analytics/statistics, strong scenario tuning and ML-based detection; good where data-science depth matters |
| **Oracle FCCM (Mantas)** | Enterprise-scale, deeply configurable behaviour-detection scenarios; heavy but very common in large banks |
| **Quantexa** | **Entity resolution + network analytics** — connects data into a graph to reveal hidden relationships; contextual, low-false-positive, "big-picture" risk |
| **Napier** | Modern, cloud-native, AI-driven; fast deployment, strong for fintechs/mid-tier; configurable rules + ML |

Actimize/Oracle/SAS = the incumbents (rule-heavy). Quantexa/Napier = the new wave (network + ML, aiming at the false-positive problem).

**The false-positive problem:** rules-based TM typically produces **90–98% false positives** — most alerts are legitimate activity. This drives huge analyst cost, so **tuning** (adjusting thresholds via Above/Below-the-Line testing) and **ML risk-scoring** (ranking alerts by probability of being genuine) are central. **Network analytics** cuts false positives by adding context — a lone "large wire" alert looks different once you see the counterparty is a known mule cluster.

## Hands-on — step by step

**Alert:** Account of **"Kiran Textiles"** (KYC: declared annual turnover ₹2 crore, retail garment trader). TM scenario **"High-velocity pass-through"** fires.

**Step 1 — Read the alert.**
```
Scenario: Rapid movement of funds (pass-through)
Trigger:  Inbound ₹18,50,000 (5 credits) then ₹18,20,000 debited within 36h
Period:   1–3 July 2026 | Alert score: 78/100
```

**Step 2 — Gather context (the triage checklist):**
- **KYC/profile:** declared turnover ₹2 cr/yr ⇒ ~₹16.6 lakh/month expected. This is ₹18.5 lakh in **3 days** — a large deviation.
- **Counterparties:** 5 inbound credits from *individuals* (not trade debtors); outbound single wire to a **new payee** in a different state.
- **History:** account previously ran ₹3–5 lakh/month steady; this is a spike.
- **Cash vs transfer:** all electronic (rules out simple structuring but fits **mule/pass-through**).

**Step 3 — Score & hypothesise.** Deviation from profile + inbound from unrelated individuals + near-total same-week sweep to a new payee = classic **flow-through / possible mule** pattern. Alert score 78 plus contextual red flags → **escalate to case**, do not auto-close.

**Step 4 — Investigate the network.** Pull the entity graph: the new outbound payee also receives from **three other flagged accounts** → a **fan-in/fan-out mule ring**. Network analytics converts a single ambiguous alert into a strong typology.

**Step 5 — Request info / decide.** Raise an RFI to the business for supporting invoices for the ₹18.5 lakh. Inadequate/absent commercial rationale + ring linkage → **file STR** within 7 working days (Chapter 1), continue enhanced monitoring, and consider exit per policy. **Do not tip off.**

**Step 6 — Feed back to tuning.** Log the disposition. Confirmed-suspicious outcomes validate the scenario; if this segment throws many *false* positives, propose a threshold review (e.g., raise velocity floor for genuine wholesale traders) through governed **ATL/BTL testing** — never ad-hoc.

## The output

**TM Case Summary — Kiran Textiles**

```
Alert: SAM-2026-77120 | Scenario: Rapid movement / pass-through | Score 78
Profile: garment trader, declared ₹2cr/yr (~₹16.6L/mo)
Observed: ₹18.5L in over 3 days (5 unrelated individuals) → ₹18.2L swept
          to new out-of-state payee in 36h
Red flags: profile deviation; unrelated inbound; new payee; near-total sweep
Network: outbound payee linked to 3 other flagged accounts → mule ring
RFI: invoices requested — none provided
DECISION: Escalate → STR filed (7 wd) → enhanced monitoring → exit review
Tuning note: scenario validated; no threshold change for this segment
Investigator: [id] | QA: [id] | 15-Jul-2026
```

## Checks, gotchas & red flags

- **An alert is not a conclusion** — it's a question. Investigate against KYC profile before disposing.
- **Profile deviation is the strongest single signal** — always compare activity to declared turnover/expected behaviour.
- **Electronic ≠ clean** — pass-through/mule laundering is all transfers; don't dismiss just because there's no cash.
- **Never auto-close a high-score alert** without documented rationale; equally, don't escalate everything (alert fatigue hides real ones).
- **Tuning is governed** — thresholds change only via ATL/BTL testing with sign-off; silently loosening a rule to cut volume can create **false negatives** (missed laundering) and is an audit finding.
- **Look at the network**, not just the account — mule rings are invisible one account at a time.
- **STR timeline (7 working days)** starts when suspicion is *established*, not when the alert first fires — but don't sit on it.
- **Don't tip off** the customer while investigating or after filing.

## Interview drill

**Q1: Why do rules-based TM systems generate so many false positives, and how do you reduce them?**
Rules are deliberately broad to avoid missing genuine cases, so they flag lots of legitimate activity — typically 90%+ of alerts are false positives. You reduce them by segmenting customers and tuning thresholds per segment via Above/Below-the-Line testing, by layering ML risk-scoring to rank alerts, and by adding network/entity context so an alert is judged against relationships, not in isolation — which is exactly what tools like Quantexa target.

**Q2: Walk me through triaging a "rapid movement of funds" alert.**
I compare the activity to the customer's KYC profile and expected turnover, examine the counterparties (are inbound credits from known trade parties or unrelated individuals?), check the account's history for deviation, and look at whether funds were swept out almost immediately to a new payee. Then I pull the network to see if counterparties link to other flagged accounts. If there's no commercial rationale and the pattern fits mule/pass-through, I escalate to a case and, if suspicion holds, file an STR — without tipping off.

**Q3: What's the risk of tightening thresholds to cut alert volume?**
False negatives — genuine laundering slipping through undetected, which is a regulatory and reputational failure far worse than false-positive cost. That's why threshold changes go through governed Below-the-Line testing to prove you're not suppressing true alerts, with documentation and sign-off, rather than being tuned informally to make queues smaller.

## Learn/practise (free)

- **NICE Actimize, SAS, Oracle FCCM, Quantexa, Napier** all publish free product docs, scenario catalogues and webinars — read a scenario library to learn real rule logic.
- Build a **toy TM engine in Python/SQL**: generate synthetic transactions, code structuring, pass-through and velocity rules with thresholds, and count your own false-positive rate — invaluable intuition.
- **NetworkX** (Python) to build a counterparty graph and visualise a mule ring — mimics entity/network analytics for free.
- **FATF** and **Egmont Group** typology reports — the authoritative source for real laundering patterns to encode.
- **Wolfsberg Group** statement on effective monitoring, and ACAMS/IIBF TM modules for the investigator workflow and STR-writing practice.
