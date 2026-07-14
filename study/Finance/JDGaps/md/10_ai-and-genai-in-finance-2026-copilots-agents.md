# AI & GenAI in Finance (2026): Copilots, LLMs, Agents, Governance

## The gap

The bundles cover "AI & automation" at a general level and teach Python/pandas automation. What they do **not** cover is the **2026 GenAI-in-finance reality** that JDs now explicitly demand: the **Copilots** embedded in the tools you already use (Excel, Power BI, M365), **LLMs** used daily for research, commentary and code, **agentic automation** (Genpact's "AI Gigafactory," Accenture, Citi), the **prompt skill** that separates useful from dangerous output, and — most importantly for a finance role — the **governance, model-risk and hallucination controls** without which no bank lets you touch this. This is the gap because "used ChatGPT" is not a skill; *operating GenAI safely on financial data with controls* is.

## Why companies ask for it

> Real posting (Genpact, FP&A/R2R): a company-wide push on **"AI Gigafactory / agentic AI."**

> Earlier 2026 JDs: Accenture and Citi emphasise **agentic AI** and GenAI copilots; "multiple 2026 JDs emphasise AI/GenAI and GCC shared-services."

Every finance function is being asked to do more with the same headcount, and GenAI is the lever. The roles that name it: **FP&A analysts** (faster commentary, variance narratives), **R2R/controllers** (reconciliation triage, journal narratives), **transformation / finance-tech** teams building agents, and **GCC delivery** roles where "productivity via AI" is now a KPI. Employers are not looking for prompt engineers — they want finance people who **use these tools competently and know the guardrails.**

## What "proficient" looks like

An employer tests whether you can:

- Use **Copilot inside Excel and Power BI** to generate formulas, DAX, summaries and charts from a natural-language ask — and **verify** the output.
- Use an **LLM** to draft variance commentary, write/debug **SQL and DAX**, summarise long documents, and structure analysis — with disciplined prompting.
- Explain **agentic automation** — the difference between a chatbot, a copilot, and an autonomous agent that chains steps and calls tools.
- Articulate **AI governance**: hallucination risk, data-confidentiality rules, human-in-the-loop review, model risk, and why you never paste client data into a public model.

## How to actually learn/do it

**1. Copilots in the tools you already know.**
- **Excel Copilot (M365 Copilot):** in a table, open the Copilot pane and type "add a column flagging variances over 10%," "summarise this data," or "suggest a PivotTable." It writes the formula/PivotTable — you **check it**. Great for boilerplate; wrong often enough that verification is mandatory.
- **Power BI Copilot:** in the report view, "create a page analysing sales by region," or ask it to **write a DAX measure** ("YoY revenue growth %") or **explain an existing measure**. It also drafts narrative summaries of a visual.
- **M365 Copilot for finance:** summarise a 40-page board pack, draft an email from a variance table, generate a first-cut PowerPoint from an Excel model.
- **Free alternatives:** you don't need a paid Copilot licence to build the skill. Use **ChatGPT / Claude / Gemini free tiers** to draft the same DAX/SQL/formulas, then paste into desktop Power BI / Excel. The skill transfers.

**2. LLMs for real finance tasks — with good prompting.** The prompt pattern that works: **Role + Context + Task + Format + Constraints.** Worked example for FP&A commentary:

> "You are an FP&A analyst. Here is the Q2 variance table [paste]. Write 4 bullet points of management commentary explaining the biggest drivers of the unfavourable opex variance. Be specific, use the numbers, no speculation beyond the data."

Other daily uses: **write SQL** ("join these two tables, monthly revenue by customer"), **debug DAX**, **explain a regulation** in plain English, **reconciliation triage** (paste two lists, ask for likely mismatches), **build an Excel formula** from a description. Always: **give it the data structure, ask for its assumptions, and verify.**

**3. Agentic automation (the 2026 buzzword decoded).**
- **Chatbot** = answers questions.
- **Copilot** = assists inside an app, human drives.
- **Agent** = given a goal, it **plans steps, calls tools/APIs, and acts** with limited human checkpoints. Genpact's "AI Gigafactory" and Accenture's agentic pitch mean: an agent that, say, pulls the trial balance, runs reconciliations, drafts the journal, and flags exceptions for a human to approve. You don't have to build these, but you must **explain the concept and where human-in-the-loop sits.** Free way to grasp it: read about **Microsoft Copilot Studio agents** and **LangChain/AutoGen** concepts (no need to code them).

**4. Governance, model risk & hallucination controls — the part that gets you hired.** This is where finance credibility lives:
- **Never paste confidential/client/PII data into a public LLM.** Enterprises use walled deployments (Azure OpenAI, private endpoints) precisely for this.
- **Hallucination:** LLMs fabricate plausible numbers and citations. Rule: **the model drafts, the human owns.** Every figure is traced to source.
- **Human-in-the-loop:** any agent action with financial impact needs a review/approval gate — tie it to your **SOX/internal-controls** knowledge (four-eyes principle).
- **Model risk:** connect to model-validation vocabulary (the Acuity Model Risk JD) — versioning, testing, monitoring for drift, documentation.
- **Auditability:** prompts and outputs logged; explainability for regulators.

**5. What to put on a resume — honestly.** Do **not** write "AI/ML engineer." Do write, truthfully: "Used **Excel/Power BI Copilot** and LLMs to automate variance commentary and DAX/SQL generation, cutting reporting time by X%, with human review controls." Claim *use with judgment*, not model-building.

## How it shows up in interviews

**Q: "How have you used GenAI in a finance task?"**
A: "I use it as a fast first-drafter with verification. For monthly reporting I feed the variance table to an LLM with a structured prompt — role, the actual numbers, the format I want — to draft commentary, which I then edit and fact-check against source. I also use it to write and debug DAX and SQL. The productivity gain is real, but I treat every output as a draft I own, never a final answer."

**Q: "What are the risks of using LLMs on financial data, and how do you control them?"**
A: "Three main risks: **confidentiality** — never put client or PII data into a public model, use an enterprise walled deployment; **hallucination** — models invent plausible-but-wrong figures, so every number must trace to source and a human signs off; and **auditability** — in a controlled environment prompts and outputs should be logged. It maps cleanly onto existing SOX controls — the model is like a junior analyst whose work you always review under a four-eyes principle."

**Q: "What does 'agentic AI' mean and where's the risk?"**
A: "An agent is given a goal and autonomously plans and executes steps — calling tools and APIs — rather than just answering. In finance that might be pulling data, running a reconciliation, and drafting journals. The risk is autonomous action without oversight, so the control is human-in-the-loop approval gates on anything with financial impact, plus logging and clear ownership. The value is throughput; the discipline is governance."

## ATS keywords to add

GenAI, generative AI, LLM, Microsoft 365 Copilot, Excel Copilot, Power BI Copilot, Copilot Studio, prompt engineering, ChatGPT / Claude / Gemini, Azure OpenAI, agentic AI, AI agents, human-in-the-loop, AI governance, model risk, hallucination controls, responsible AI, RAG (retrieval-augmented generation), finance automation, AI-assisted reporting, natural-language querying, DAX/SQL generation, data confidentiality, auditability.
