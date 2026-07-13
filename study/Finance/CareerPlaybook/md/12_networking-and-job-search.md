# Networking & the finance job search

## What it is & where it's used

The "finance job search" is a distribution problem, not a knowledge problem. You already have the domain skills (from earlier chapters). This chapter is about *how a role travels from a hiring manager's head to your inbox* — and how to intercept it. It applies to every finance/accounts/tax role you'll target in India and abroad: FP&A analyst, accounts executive, GST/direct-tax associate, credit analyst, treasury, audit, equity research, investment banking, and controllership.

The uncomfortable data point: in India, roughly **30–40% of white-collar hires happen through referrals**, and at analyst/associate finance levels it's higher because managers trust "someone vouched for them" over a resume they can't verify. Job portals (Naukri, LinkedIn, Indeed) and campus placement fill most of the rest; cold outreach and recruiters fill the gaps. Globally the shape is identical — LinkedIn and employee referral programs dominate. So the skill being taught here is **manufacturing referrals and warm intros on demand**, plus running applications like a pipeline instead of a lottery.

## The gap: why companies want this (and college didn't teach it)

MBA placement cells and CA articleship create a dangerous illusion: that jobs *arrive*. You register, a company visits, you interview, you get placed. That machine works exactly once. The moment you're an off-campus, lateral, or Direct-Entry candidate, nobody delivers roles to you — and most graduates freeze because they were never taught the mechanics of self-sourced hiring.

The specific gaps:

- **Nobody taught you the hidden market.** A large share of roles are filled before they're publicly posted, or posted only for compliance after an internal referral already exists.
- **You were taught to "apply," not to route.** Blasting 200 applications on Naukri yields a ~2% callback because you're a stranger in an ATS keyword pile.
- **You think networking = asking for a job.** It doesn't. It's asking for *information and a 15-minute conversation*, which incidentally produces referrals.
- **No one showed you a recruiter is a channel, not a friend.** They're paid by the employer to fill a specific req — you must speak in their currency (fit, salary, notice period).

## What "proficient" looks like

A job-ready candidate can, unaided:

- Build a **target list of 30–50 companies** and identify the actual hiring manager (not just HR) for each.
- Write a cold message that gets a **20%+ reply rate** because it's specific, short, and asks for one small thing.
- Convert a stranger into a **referral inside 2–3 touches** without ever bluntly begging for a job.
- Run an **application tracker** (a pipeline) with follow-up dates, and treat it like a sales funnel.
- Tailor a resume to a specific JD so it **clears the ATS** and reads as an obvious fit.
- Handle a recruiter call crisply: current CTC, expected CTC, notice period, reason for change, in under 90 seconds.

The bar is behavioural: can you generate 3 warm conversations this week from a cold start? A proficient job-seeker can.

## Hands-on: how to actually do it

### 1. Build the target-company tracker (your CRM)

Use a Google Sheet. These formulas make it a live pipeline.

Days since you applied / last touched, and an auto "FOLLOW UP" flag:

```
=TODAY()-B2                                          // days since last contact (B2 = date)
=IF(AND(C2="Applied", (TODAY()-B2)>7), "FOLLOW UP", "")   // C2 = stage
```

Pull the hiring manager's name into your message template automatically:

```
=SUBSTITUTE("Hi {name}, I saw the {role} opening at {co}", "{name}", D2)
```

In Excel, count how your funnel is converting:

```
=COUNTIF(C:C,"Applied")            // top of funnel
=COUNTIF(C:C,"Interview")/COUNTIF(C:C,"Applied")   // application→interview rate
```

Columns to keep: `Company | HM Name | Role | Source | Date | Stage | Referral? | Next action | Notes`.

### 2. Find the actual hiring manager

LinkedIn search string (paste into the search bar):

```
"FP&A" AND ("hiring" OR "manager") AND "Bangalore"
```

Or use LinkedIn filters: **People → Current company = [Target] → Title contains "Finance Manager" / "Controller" / "Team Lead – Accounts".** Guess their email with the company's pattern (`firstname.lastname@company.com` is the most common in India), then verify format against any public email from the domain.

### 3. The cold message that actually works

Structure = **specific hook → credibility in one line → one small ask.** Keep it under 90 words.

```
Subject: FP&A Analyst role — quick question

Hi Priya,

I saw Zomato is hiring an FP&A Analyst. I'm an MBA (Finance) +
CA-Inter, and I recently built a 3-statement model + variance
dashboard in Excel/Power BI for a D2C P&L (happy to share).

Before I apply, could I ask you one thing — is this role more
about monthly-close reporting or forward budgeting? Want to make
sure my application speaks to what your team actually needs.

Thanks either way,
Sai  | linkedin.com/in/...
```

Why it works: you did homework, you proved output, and the ask ("one question") is trivially easy to answer — which starts a conversation that ends in a referral.

### 4. The referral ask (touch 2 or 3, never touch 1)

Never open with "refer me." Earn it first, then:

> "This was really helpful, thank you. I'm going to apply — would you be comfortable referring me internally? Totally fine if not. If it helps, here's a 3-line summary you can paste and my resume attached."

Make it **zero-effort** for them: give the paste-ready blurb and the file. That single move roughly doubles referral conversion.

### 5. Beat the ATS on the application itself

ATS (Naukri RMS, Workday, Greenhouse) rank on keyword match. Mirror the JD's exact nouns. Quick keyword-gap check in Python:

```python
jd = open("jd.txt").read().lower().split()
cv = open("resume.txt").read().lower().split()
missing = set(jd) - set(cv)
for w in ["reconciliation","variance","gst","tds","forecasting","sql","excel"]:
    print(w, "MISSING" if w in missing else "ok")
```

Add the missing (true) skills verbatim to your resume. Use a single-column, no-graphics `.docx` — ATS parsers choke on tables and text boxes.

## Worked example / mini-project

**Goal:** land interviews for an FP&A / Accounts Analyst role in Bengaluru in 3 weeks, from a cold start.

**Week 1 — Build & source.** List 40 companies (mix of MNC GCCs, startups, mid-cap manufacturers). For each, find one hiring manager on LinkedIn. Tracker snapshot:

| Company | HM | Role | Source | Stage | Referral? |
|---|---|---|---|---|---|
| Zomato | Priya S. | FP&A Analyst | LinkedIn | Messaged | Pending |
| Tata Elxsi | Rajesh N. | Accounts Exec | Naukri | Applied | No |
| Razorpay | Meera K. | Finance Analyst | Referral | Interview | Yes |

**Week 2 — Outreach.** Send 8 cold messages/day (5 days = 40). Realistic funnel:

| Stage | Count | Rate |
|---|---|---|
| Messages sent | 40 | — |
| Replies | 9 | 22% |
| Calls/chats | 4 | — |
| Referrals secured | 3 | — |
| Direct applications | 40 | — |

**Week 3 — Convert.** 3 referrals + 40 applications. A referred application at analyst level converts to a first-round interview at roughly **40–50%** vs **~2–3%** cold. Expected interviews: `(3 × 0.45) + (40 × 0.025) ≈ 1.35 + 1.0 = ~2.4`. So ~2–3 interviews in three weeks — and note that **the 3 referrals produced as many interviews as 40 blind applications.** That single insight is the entire chapter.

**CTC math for the negotiation** (know this cold before any recruiter call):

```
Current CTC ₹6,00,000 → target +30% = ₹7,80,000
In-hand ≈ CTC − PF(both sides) − prof.tax − income tax
Anchor high but justified; state expected CTC as a range: ₹7.5–8.5L
```

## How it's tested

The "test" here is the process itself, but employers do screen on adjacent skills. Expect:

**Recruiter phone screen (5–10 min), verbatim questions:**
- "Walk me through your resume in 2 minutes." (Have a rehearsed 90-sec pitch.)
- "Current CTC, expected CTC, notice period?"
- "Why are you looking to change / why this role?"
- "Are you comfortable with [location / shift / CTC band]?"

**Behavioural / fit round:**
- "Tell me about a time you handled a tight deadline." (Use STAR: Situation-Task-Action-Result.)
- "Why our company specifically?" — this is where your networking research pays: name the team, the product, something real.

**The practical screen** (role-dependent, covered in earlier chapters): a timed Excel test, a SQL query screen, or a "close these books / reconcile this ledger" case. Networking gets you *to* the test; it doesn't replace it.

## Common mistakes & how pros avoid them

| Mistake | What pros do |
|---|---|
| Blasting 200 identical applications | 40 targeted, each with a tailored resume + a referral attempt |
| Opening a cold DM with "please refer me" | Ask a smart question first; earn the referral over 2–3 touches |
| Long, generic messages ("I am a passionate finance professional…") | Under 90 words, specific hook, one small ask |
| Treating recruiters as career counsellors | Speak their currency: fit, CTC, notice period, availability |
| No follow-up | Follow up once after 5–7 days; ~30% of replies come from the nudge |
| Networking only when unemployed | Keep 5 warm contacts alive year-round — the best time to network is before you need it |
| Lying about CTC/notice | Recruiters verify via payslips/relieving letters; inflating gets offers revoked |
| Ignoring the ATS | Mirror JD keywords, single-column .docx, no tables/graphics |

## Learn-it roadmap & resources

**Time to proficiency: 2–4 weeks of active practice** (this is a *doing* skill, not a studying skill).

| Week | Focus |
|---|---|
| 1 | Build tracker + target list; optimise LinkedIn profile (banner, headline with keywords, "Open to Work") |
| 2 | Send 40 cold messages; do 3 informational chats |
| 3 | Convert to referrals + applications; run the funnel |
| 4 | Interview prep, follow-ups, negotiation rehearsal |

**Resources:**
- *LinkedIn* — free; your primary sourcing + outreach tool. Complete the profile to "All-Star."
- *Naukri / Indeed / iimjobs (for finance/consulting) / Instahyre* — India job boards; iimjobs and Instahyre skew higher for MBA-finance roles.
- Company career pages + **GCC (Global Capability Centre) portals** — Bengaluru/Hyderabad/Pune are packed with MNC finance shared-service roles.
- *Naukri "Recruiter Connection"* and LinkedIn Recruiter InMails — respond fast; recruiters work FIFO.
- Books: *Never Eat Alone* (Ferrazzi) for networking mindset; *Cracking the finance interview* guides for role-specific prep.
- Certification signal: your **CA-Inter + MBA** already clears most screens — no extra networking cert needed. Spend the money on a Power BI / SQL cert instead (covered earlier), which makes your cold messages credible.

## Quick-reference

| Item | Value / formula |
|---|---|
| Referral share of hires (India) | ~30–40% |
| Referred vs cold interview conversion | ~45% vs ~2–3% |
| Cold message length | < 90 words, one ask |
| Reply rate to aim for | 20%+ |
| Follow-up timing | once, after 5–7 days |
| Outreach cadence | 8 messages/day |
| Days-since-touch flag | `=IF((TODAY()-B2)>7,"FOLLOW UP","")` |
| Funnel conversion | `=COUNTIF(C:C,"Interview")/COUNTIF(C:C,"Applied")` |
| Email guess pattern (India) | `firstname.lastname@company.com` |
| Recruiter screen essentials | Current CTC · Expected CTC · Notice period · Reason for change |
| Referral ask rule | Never touch #1; give paste-ready blurb + resume |
| Resume format for ATS | Single-column .docx, JD keywords mirrored, no tables |
| Negotiation anchor | +25–35% on current CTC, stated as a range |
| STAR | Situation → Task → Action → Result |
