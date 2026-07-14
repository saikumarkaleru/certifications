# GenAI for Finance Workflows: Copilots, LLMs & Prompting

## What you'll be able to do

By the end of this chapter you can sit at a real finance desk and use generative AI as a competent junior analyst: turn a Copilot in Excel/Power BI into a formula-and-DAX author, draft month-end variance commentary from a numbers table, summarise a 40-page annual report or RBI circular into a decision-ready brief, generate and debug SQL/DAX/VBA you can read and trust, clean messy vendor master data, and — critically — *verify* every output before it leaves your hands. You will know exactly which finance tasks GenAI accelerates safely, which it must never do unsupervised, and the prompt patterns that get first-time-right results.

## The essentials

A large language model (LLM) predicts the next token from your prompt plus its training data. It is a **language** engine, not a **calculation** engine: it drafts, summarises, translates, and codes brilliantly, but its arithmetic on free text is unreliable. So the rule for finance is: **let the LLM write the logic (formula, query, commentary), let a deterministic tool (Excel, SQL engine, calculator) do the maths.**

Tools you'll actually meet in an India GCC / analyst seat (mid-2026):

| Tool | What it does | Access / cost (2026) |
|---|---|---|
| **Microsoft 365 Copilot** | Sits in Excel, Word, Outlook, Teams, PowerPoint; drafts, summarises emails/meetings, writes Excel formulas & pivot suggestions | Paid add-on, ~US$30/user/mo on top of a M365 licence; enterprise-provisioned |
| **Copilot in Excel** | Natural-language → formulas, PivotTables, conditional formatting, "explain this workbook", basic Python-in-Excel | Part of M365 Copilot; needs data in a Table |
| **Copilot in Power BI / Fabric** | Generate DAX measures, "create a report page for revenue by region", narrative summaries of visuals | Fabric capacity (F-SKU) or PPU licence |
| **ChatGPT / Claude / Gemini (enterprise)** | General research, drafting, code, data cleaning via chat or API | Enterprise tiers keep your data out of training; free tiers do NOT |
| **Copilot free / Bing** | The free way to practise all prompt patterns below | Free with a Microsoft account |

**Data-privacy non-negotiable:** never paste unpublished financials, PII, MNPI (unpublished price-sensitive information under SEBI PIT Regulations), or client data into a *consumer* GenAI tool. Use only the enterprise instance your employer sanctions, where data isn't retained for training. When practising at home, use synthetic or already-public numbers.

## Hands-on — step by step

Worked scenario: you're closing **June 2026** for a mid-cap. Actual revenue ₹1,240 lakh vs budget ₹1,150 lakh; actual opex ₹910 lakh vs budget ₹860 lakh.

**1. Copilot in Excel — write a formula.** Put your data in a Table (Ctrl+T). Open the Copilot pane (Home ribbon → Copilot). Prompt:

> "Add a column 'Variance %' = (Actual − Budget) / Budget, formatted as a percentage with one decimal, and flag values worse than −5% for expenses as 'Investigate'."

Copilot returns something like `=(B2-C2)/C2` and offers to insert the column. **Read the formula** — is Budget the denominator, sign convention correct? Insert, then eyeball one row by hand: (1240−1150)/1150 = 7.8%. Ties out.

**2. LLM for variance commentary.** Paste the *computed* variance table (numbers already correct in Excel) into your enterprise LLM:

> "You are an FP&A analyst. Below is June-26 actual vs budget (₹ lakh). Write 4 bullet points of variance commentary for the CFO: state the driver direction, quantify in ₹ lakh and %, and flag anything needing action. Neutral, factual tone. Do not invent causes — where a cause isn't given, say 'driver to be confirmed with business.'"
> Revenue: Actual 1240, Budget 1150. Opex: Actual 910, Budget 860.

The "do not invent causes" clause is what stops hallucinated narratives.

**3. Draft DAX / SQL / VBA.** In Power BI Copilot:

> "Create a DAX measure 'Rev Var %' = DIVIDE(SUM(Actual[Rev]) − SUM(Budget[Rev]), SUM(Budget[Rev])). Handle divide-by-zero."

You get `Rev Var % = DIVIDE(SUM(...)-SUM(...), SUM(...), BLANK())`. For SQL, prompt a chat LLM: *"Write ANSI SQL to return top 10 customers by FY26 revenue from table sales(cust_id, invoice_dt, amount); FY = Apr–Mar."* Then **run it against a test set** before production.

**4. Data cleaning.** Paste a messy vendor list:

> "Standardise these vendor names to Title Case, strip 'Pvt Ltd/Private Limited' variants to 'Pvt Ltd', and list suspected duplicates. Return a two-column table: original | cleaned."

Use the mapping to build a lookup — never let the LLM silently overwrite a master.

**Prompt patterns worth memorising (RTCF):** **R**ole ("You are a treasury analyst"), **T**ask (one verb, one deliverable), **C**ontext (the data, the accounting standard, the currency), **F**ormat ("as a 3-column markdown table"). Add **constraints** ("cite the row", "don't invent numbers", "flag uncertainty").

## The output

The June commentary Copilot/LLM produces, after your review:

> **June-2026 Actual vs Budget — CFO note (₹ lakh)**
> - **Revenue ₹1,240 vs ₹1,150 budget: +₹90 (+7.8%)** — favourable; driver to be confirmed with business (volume vs price split not provided).
> - **Opex ₹910 vs ₹860 budget: +₹50 (+5.8%) adverse** — spend above plan; exceeds the −5% expense threshold, flagged for investigation.
> - **Net contribution ₹330 vs ₹290 budget: +₹40 (+13.8%)** — revenue upside outweighs cost overrun.
> - **Action:** confirm revenue driver and the ₹50 lakh opex overrun with cost-centre owners before sign-off.

Deliverable = a clean Excel table with a correct, self-checking `Variance %` column, a reusable DAX measure, and a CFO-ready paragraph — drafted in minutes, verified by you.

## Checks, gotchas & red flags

- **Never trust LLM arithmetic on free text.** It will confidently return 7.2% where Excel says 7.8%. Compute in the sheet; use the LLM only to *narrate* computed numbers.
- **Hallucinated citations / causes.** LLMs invent plausible drivers ("higher marketing spend") that never happened. Force "driver to be confirmed" where data is silent.
- **Stale knowledge.** A model's training cutoff means it may quote the *old* tax slab, an outdated Ind AS, or a superseded RBI limit. Verify anything rules-based against the live source (incometax.gov.in, RBI, ICAI).
- **Privacy breach.** Pasting MNPI or client PII into a consumer tool can be a SEBI/DPDP Act violation and grounds for dismissal. Enterprise instance only.
- **Silent overwrites in data cleaning.** Always keep original + cleaned side by side; a "helpful" standardisation can merge two genuinely different vendors.
- **Copilot needs structured input.** Data must be in a proper Excel Table or a clean model; on merged cells and blank rows it fails or guesses.
- **Explainability.** If you can't read the DAX/SQL it wrote, you can't own it. Ask it to "explain this line by line" until you can.

## Interview drill

**Q1: "Your manager says 'just have ChatGPT write our quarterly variance report.' What do you do?"**
A: I'd use GenAI as a drafting assistant, not the author of record. I compute all variances in the model so the maths is deterministic, feed the *verified* numbers to an enterprise LLM with a role/format prompt and an explicit "don't invent drivers" constraint, then review every line against source, add the real business drivers from cost-centre owners, and take ownership before it goes to the CFO. I'd also confirm we're on the sanctioned enterprise tenant so no unpublished financials train a public model.

**Q2: "Where does an LLM genuinely save an analyst time, and where is it dangerous?"**
A: Big wins: drafting commentary and emails, summarising long filings/circulars, writing first-draft SQL/DAX/VBA, and cleaning/standardising text data. Dangerous: doing the arithmetic, applying tax/accounting rules from memory (training cutoff risk), and anything touching MNPI or PII in a non-enterprise tool. The pattern is language-tasks yes, calculation-and-compliance-of-record no.

**Q3: "How do you stop hallucinations in a finance workflow?"**
A: Ground it — give the model the actual data/document rather than asking from memory (RAG), constrain the output ("cite the row/section", "say 'unknown' if not present"), keep computation in a deterministic engine, and always human-verify against the primary source before use.

## Learn/practise (free)

- **Copilot free / Microsoft Copilot** (copilot.microsoft.com) and **Excel's built-in "Analyze Data"** — rehearse formula and pivot prompts with public data.
- **ChatGPT / Claude / Gemini free tiers** — practise RTCF prompts using *synthetic* numbers only.
- **DAX:** Microsoft Learn "Copilot in Power BI" module + SQLBI free articles; verify every generated measure in Power BI Desktop (free).
- **Prompting:** Microsoft "Copilot Lab" prompt gallery, Anthropic's free prompt-engineering guide, Google's "Prompting essentials".
- **Rehearsal drill:** take any listed company's annual report (public), ask the LLM for a 10-bullet summary, then fact-check each bullet against the PDF — this trains both prompting and the verification reflex employers want.
