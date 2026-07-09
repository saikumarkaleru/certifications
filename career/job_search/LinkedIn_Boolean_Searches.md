# LinkedIn Boolean Job Searches — Saikumar Kaleru

Ready-to-paste **Boolean search strings** for every role we've built resumes for, across Finance,
Business Development, and IT/Software. Paste a string into the LinkedIn **Jobs** search bar.

> These are LinkedIn **Boolean** strings (OR / AND / NOT + quotes + parentheses) — not literal regex.
> LinkedIn matches these against job **title + description**, so also use the filters below.

---

## How to use (30 seconds)
1. LinkedIn → search bar → paste a string → **Enter** → click the **Jobs** tab.
2. Set filters: **Experience level = Entry level / Internship**, **Date posted = Past 24 hours/week**,
   **Location = Hyderabad / India** (or turn on **Remote**).
3. Save the search → enable **alerts** so new posts come to you.

### Rules
- `OR`, `AND`, `NOT` must be **UPPERCASE**. Wrap multi-word titles in **"quotes"**. Group with **( )**.
- Keep strings reasonably short — very long Boolean can get truncated. If a string misfires, keep only
  the first 3–4 titles.
- Prefer the **Experience-level filter** over typing "fresher" (many entry jobs don't use that word).

### Reusable modifiers (append with AND / NOT)
```
Fresher tilt:     AND ("Fresher" OR "Entry Level" OR "Graduate" OR "Trainee" OR "Associate" OR "Junior")
Exclude senior:   NOT "Senior" NOT "Lead" NOT "Principal" NOT "Staff" NOT "Manager" NOT "Head"
Remote only:      AND ("Remote" OR "Work from home" OR "WFH")
Location tilt:    AND ("Hyderabad" OR "Bangalore" OR "Bengaluru" OR "India")
```

---

## 🏦 FINANCE ROLES

**Equity Research**
```
"Equity Research" OR "Research Analyst" OR "Equity Analyst" OR "Investment Research" OR "Fundamental Analyst"
```
**Financial Analyst / FP&A**
```
"Financial Analyst" OR "FP&A" OR "Financial Planning and Analysis" OR "Finance Analyst" OR "Business Finance"
```
**Quant / Derivatives Analyst**
```
"Quantitative Analyst" OR "Quant Analyst" OR "Derivatives Analyst" OR "Quantitative Research" OR "Quant Researcher"
```
**Risk Analyst (Market & Credit)**
```
"Risk Analyst" OR "Market Risk" OR "Credit Risk" OR "Risk Management" OR "Risk Associate"
```
**Technical Research**
```
"Technical Analyst" OR "Technical Research" OR "Market Analyst" OR "Trading Analyst"
```
**Credit Rating Analyst**
```
"Credit Rating" OR "Rating Analyst" OR "Ratings Analyst" OR "Credit Analyst"
```
**Credit Analyst (Corporate / NBFC)**
```
"Credit Analyst" OR "Credit Underwriter" OR "Credit Risk Analyst" OR "Corporate Credit" OR "Credit Manager"
```
**Wealth Management / Investment Advisory**
```
"Wealth Manager" OR "Relationship Manager" OR "Investment Advisor" OR "Investment Adviser" OR "Private Banking" OR "Financial Advisor"
```
**Investment Banking**
```
"Investment Banking" OR "Investment Banking Analyst" OR "M&A Analyst" OR "Corporate Finance" OR "IB Analyst"
```
**Product Control / Financial Control**
```
"Product Control" OR "Product Controller" OR "Financial Control" OR "Financial Controller" OR "P&L Control"
```
**Treasury Analyst**
```
"Treasury Analyst" OR "Treasury Associate" OR "Treasury" OR "Cash Management" OR "Liquidity Analyst"
```
**Investment Operations / Middle Office**
```
"Investment Operations" OR "Middle Office" OR "Trade Support" OR "Trade Operations" OR "Securities Operations"
```
**Fund Accounting**
```
"Fund Accountant" OR "Fund Accounting" OR "Fund Administration" OR "Fund Administrator" OR "NAV"
```
**KYC / AML / Financial Crime**
```
"KYC" OR "AML" OR "Anti Money Laundering" OR "Financial Crime" OR "Transaction Monitoring"
```
**Investor Relations**
```
"Investor Relations" OR "IR Analyst"
```
**ESG / Sustainability**
```
"ESG Analyst" OR "ESG" OR "Sustainability Analyst" OR "Sustainable Finance" OR "ESG Research"
```

**Finance — wide net (one search):**
```
("Financial Analyst" OR "Equity Research" OR "Credit Analyst" OR "Risk Analyst" OR "Investment Banking" OR "Treasury" OR "Fund Accounting") AND ("Analyst" OR "Associate")
```

---

## 💼 BUSINESS DEVELOPMENT / SALES ROLES

**Financial-Services / Fintech BD** (uses your NISM + finance edge)
```
("Business Development" OR "Relationship Manager" OR "Sales" OR "Inside Sales") AND ("Financial" OR "Fintech" OR "Banking" OR "Wealth" OR "Insurance" OR "Mutual Fund" OR "Broking")
```
**Fintech / SaaS Sales (SDR / BDR)**
```
"Sales Development Representative" OR "SDR" OR "Business Development Representative" OR "BDR" OR "Inside Sales" OR "SaaS Sales" OR "Account Executive"
```
**General Business Development**
```
"Business Development Executive" OR "Business Development" OR "BDE" OR "Sales Executive" OR "Inside Sales" OR "Sales Associate"
```

---

## 💻 IT / SOFTWARE ROLES

**Software Engineer (SDE)**
```
"Software Engineer" OR "Software Developer" OR "SDE" OR "Software Development Engineer" OR "Associate Software Engineer"
```
**C++ / Low-Latency Systems**
```
("C++ Developer" OR "C++ Engineer" OR "Software Engineer" OR "Systems Engineer") AND ("C++" OR "Low Latency" OR "HFT" OR "Trading Systems")
```
**Quant Developer**
```
"Quant Developer" OR "Quantitative Developer" OR "Quant Dev" OR "Trading Systems Developer" OR "Quantitative Software"
```
**DevOps / SRE / Cloud**
```
"DevOps" OR "Site Reliability" OR "SRE" OR "Platform Engineer" OR "Cloud Engineer" OR "Infrastructure Engineer"
```
**Backend Developer**
```
"Backend Developer" OR "Backend Engineer" OR "Back End Developer" OR "API Developer" OR "Python Developer"
```
**Full-Stack / Web**
```
"Full Stack" OR "Fullstack" OR "Full Stack Developer" OR "Web Developer" OR "MERN" OR "React Developer"
```
**Data Engineer**
```
"Data Engineer" OR "Data Engineering" OR "ETL Developer" OR "Analytics Engineer" OR "Big Data Engineer"
```
**Data / BI Analyst** (bonus — fits your SQL + Power BI)
```
"Data Analyst" OR "Business Intelligence" OR "BI Analyst" OR "Business Analyst" OR "Reporting Analyst"
```

**IT — wide net (one search):**
```
("Software Engineer" OR "Software Developer" OR "Backend" OR "Full Stack" OR "Data Engineer" OR "DevOps" OR "SDE") AND ("Java" OR "Python" OR "C++")
```

---

## 🎯 Skill-restricted examples (grouping with parentheses + AND)
```
("Data Engineer" OR "ETL Developer" OR "Analytics Engineer") AND ("Python" OR "SQL")
("Backend Developer" OR "Software Engineer") AND ("Python" OR "FastAPI" OR "Django")
("Quant Developer" OR "Quantitative Analyst") AND ("C++" OR "Python")
("DevOps" OR "SRE") AND ("Kubernetes" OR "Docker" OR "Jenkins" OR "AWS")
("Relationship Manager" OR "Business Development") AND ("Wealth" OR "Mutual Fund" OR "NISM")
```

## ⚠️ Notes
- LinkedIn Boolean works in the **keywords** box; use the separate **Title**, **Experience level**,
  **Location**, and **Remote** filters to sharpen results (don't cram everything into Boolean).
- If a long string returns nothing, LinkedIn likely truncated it — shorten to the top 3–4 titles.
- Naukri, Indeed, and Instahyre support the same OR/AND quoting — these strings mostly port over.
- Save each search as an **alert** so fresh postings reach you first (huge edge on entry-level roles).
