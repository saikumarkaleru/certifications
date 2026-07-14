# AI Agents, RAG & Governance in Finance

## What you'll be able to do

You'll be able to explain and reason about the three things a 2026 finance employer means when they say "we're deploying AI": **agentic automation** (AI that takes multi-step actions in finance operations), **RAG** (retrieval-augmented generation — an LLM answering strictly from *your* documents and policies), and **AI governance** (model risk, hallucination control, data privacy, and regulatory compliance including the EU AI Act). You'll be able to sketch how a RAG assistant over a policy library actually works, describe a realistic agentic invoice-to-pay or reconciliation workflow, name what leading firms (Genpact, Accenture, Citi) are actually doing, and — the part that gets you hired into a GCC or compliance/model-risk seat — articulate the *controls* that make any of this safe.

## The essentials

**RAG in one line:** instead of relying on what the model memorised, you retrieve the relevant chunks from *your* trusted documents and paste them into the prompt, so the answer is grounded in — and citable to — your data.

The RAG pipeline:

| Stage | What happens |
|---|---|
| **Ingest** | PDFs/policies/contracts split into chunks (~300–800 tokens) |
| **Embed** | Each chunk → a vector (embedding) capturing meaning |
| **Store** | Vectors go into a vector DB (e.g. Azure AI Search, Pinecone, pgvector) |
| **Retrieve** | User question is embedded; nearest chunks are fetched |
| **Generate** | LLM answers using *only* those chunks, with citations |

RAG is how you get "Which vendors have net-45 payment terms per our contracts?" answered from the actual contracts, with source links — and how you *stop* hallucination, because the model is told "answer only from the provided context; if not present, say you don't know."

**AI agents** go one step further: an LLM that can *plan* and *call tools* (query a DB, post to an API, send an email, raise a ticket) in a loop until a goal is met. In finance ops this looks like:

- **Invoice-to-pay:** agent reads an invoice, extracts fields, matches to PO and GRN (3-way match), flags mismatches, drafts the posting — human approves.
- **Reconciliation:** agent pulls bank and ledger, matches transactions, proposes journal entries for breaks.
- **Close support:** agent gathers variance data, drafts commentary, chases open items.

Crucially, safe agents run **human-in-the-loop** for anything that moves money or hits the ledger, and with **least-privilege** access (read-mostly, scoped credentials).

**Where the industry is (2026):**
- **Genpact** — "agentic AI" for finance & accounting BPO; agents for invoice processing, collections, and close, sold as outcome-based services.
- **Accenture** — reinvention services + a large trained AI workforce; RAG "knowledge assistants" over client policy and control libraries.
- **Citi / global banks** — internal GenAI assistants (document search, coding, research summarisation) rolled out to tens of thousands of staff, kept inside a governed, private environment; heavy model-risk oversight.

## Hands-on — step by step

You can't run a bank's stack at home, but you can build the exact pattern. Scenario: a **RAG assistant over your company's Travel & Expense policy** so employees stop emailing finance "can I claim airport lounge access?"

1. **Collect the source** — the T&E policy PDF (public/synthetic for practice).
2. **Chunk it** — split by section/heading into ~500-token pieces; keep the section title with each chunk (helps citation).
3. **Embed** — run each chunk through an embedding model (e.g. Azure OpenAI `text-embedding-3-small`, or a free local model via `sentence-transformers`).
4. **Store** — load vectors into a vector store. For practice, `pgvector` on free Postgres, or an in-memory FAISS index in Python.
5. **Query** — embed the question "Is airport lounge access reimbursable?", retrieve top-4 chunks.
6. **Generate with guardrails** — prompt:
   > "Answer the employee's question using ONLY the policy sections below. Quote the clause and its section number. If the policy does not cover it, reply: 'Not specified in policy — check with Finance.' Do not guess."
7. **Show citations** — return the answer plus the section it came from, so a human can verify.

For the **agentic** flavour, add a tool: if the answer is "reimbursable", the agent can *draft* (not submit) a claim in the expense system, leaving final submission to the employee. That "draft, don't submit" boundary is the governance point.

## The output

The RAG assistant's response, as a user sees it:

> **Q: Is airport lounge access reimbursable?**
> **A:** Yes, for international travel in Manager grade and above. Per **T&E Policy §4.3 (Airport Services):** "Lounge access is reimbursable for international itineraries for employees at M3 and above, capped at ₹2,500 per visit." For domestic travel it is **not** covered (§4.3, same clause). *Source: T&E Policy v2026.1, §4.3.*

And a one-page **governance register entry** for that assistant:

> **Use case:** T&E policy Q&A (RAG). **Risk tier:** Low (informational, no payment action). **Data:** internal policy only, no PII. **Controls:** answers cited to source; "not specified" fallback; enterprise LLM (no training on our data); quarterly review of accuracy on a 20-question test set; human owner: FP&A lead. **EU AI Act relevance:** minimal-risk / limited-risk (transparency: users told it's AI).

## Checks, gotchas & red flags

- **RAG still hallucinates if retrieval is bad.** If the right chunk isn't retrieved, the model may fill the gap. Test retrieval quality, not just the final answer.
- **Chunking destroys tables.** Financial policies and filings have tables; naive splitting breaks them. Use layout-aware parsing for numbers.
- **Agents with write access are the real danger.** An agent that can post journals or release payments unsupervised is a fraud-and-error surface. Enforce human approval, maker-checker, and least privilege.
- **Data privacy (India DPDP Act 2023 + SEBI/RBI).** Personal data and MNPI must stay in a governed environment; know where the vector store and the LLM physically process data (data residency).
- **Model risk (RBI/SEBI + global norms).** Any model influencing financial decisions needs validation, monitoring, documentation, and an accountable owner — the same discipline as credit/market-risk models (think SR 11-7 / RBI model-risk expectations).
- **EU AI Act awareness.** Risk-tiered: *unacceptable* uses banned; *high-risk* (e.g. creditworthiness scoring) faces strict obligations — data governance, human oversight, transparency, logging; *limited-risk* needs disclosure that users are dealing with AI. GPAI (foundation-model) obligations phase in through 2025–2027. Even Indian GCCs serving EU clients must comply.
- **"Black box" excuse doesn't fly.** If you can't explain how the assistant reached an answer, it fails audit. Citations and logs are your defence.

## Interview drill

**Q1: "What is RAG and why does finance care?"**
A: Retrieval-augmented generation grounds an LLM in our own trusted documents: we embed our policies/filings, retrieve the relevant chunks for a question, and make the model answer only from those, with citations. Finance cares because it turns a hallucination-prone chatbot into an auditable assistant — every answer traces to a source clause, and if the source is silent the model says "unknown" instead of inventing. That auditability is what makes it usable under model-risk and compliance requirements.

**Q2: "Where would you allow an AI agent to act autonomously in finance ops, and where not?"**
A: Autonomous is fine for *read and draft* work — extracting invoice fields, matching to PO/GRN, proposing journal entries, drafting commentary — because a human still approves. I would not let an agent autonomously post to the ledger, release payments, or change master data; those need maker-checker and least-privilege credentials. The principle: agents accelerate the preparation, humans retain the control point wherever money or the books move.

**Q3: "A regulator asks how you control AI risk. What do you say?"**
A: We tier use cases by risk, keep an inventory with an accountable owner each, validate and monitor any model influencing decisions, ground answers via RAG with citations, log inputs/outputs, keep data in a governed residency-compliant environment (DPDP/RBI/SEBI), enforce human oversight on high-risk actions, and map obligations to the EU AI Act where we serve EU clients. It's the model-risk-management discipline extended to GenAI.

## Learn/practise (free)

- **Build a RAG demo free:** Python + `sentence-transformers` + FAISS, or LangChain/LlamaIndex quick-starts; Azure has a free-tier "chat over your data" sample.
- **Microsoft Learn** — "Fundamentals of Generative AI", "Implement RAG with Azure AI Search" (free modules).
- **EU AI Act** — the official EU "AI Act Explorer" / summary pages; read the risk-tier definitions and the GPAI section.
- **Model risk** — read a public summary of Fed SR 11-7 and RBI's model-governance guidance to see the control vocabulary.
- **Vendor viewpoints** — Genpact, Accenture, and BCG public "agentic AI in finance" reports (free) for real use-case framing to cite in interviews.
- **Rehearsal:** build the T&E RAG bot on a public policy PDF, deliberately ask an out-of-scope question, and confirm it says "not specified" — that demo alone is strong interview evidence.
