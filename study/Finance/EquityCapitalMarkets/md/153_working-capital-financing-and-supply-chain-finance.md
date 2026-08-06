# Working Capital Financing and Supply Chain Finance

## The Problem / Why this matters
Working capital is usually analysed as an operating variable — days of inventory, receivables and payables. But it is also *financed*, and how it is financed determines both the reported balance sheet and the company's vulnerability. Arrangements such as supply chain financing, receivables factoring and bill discounting can make a company appear to have improved its working capital when it has in substance borrowed, and reported debt can materially understate the real position.

## Core Idea
Working capital improvements should be **verified as operational rather than financial** — because a payable extended by a bank funding the supplier is borrowing presented as trade credit.

## Why it works this way
In a supply chain finance arrangement, a bank pays the company's supplier early and the company pays the bank later on extended terms. Economically the company has borrowed. Depending on the structure and disclosure, the obligation may sit in trade payables rather than in borrowings — so days payable rise, working capital improves, reported debt does not, and the underlying reality is a financing arrangement.

```mermaid
graph LR
  A[Company receives goods] --> B[Bank pays supplier early]
  B --> C[Supplier receives cash, discounted]
  C --> D[Company pays the bank on extended terms]
  D --> E[Economically: borrowing]
  E --> F[Presented as: trade payables]
```

## Full technical content

### The arrangements to look for

| Arrangement | Effect on reported numbers | The reality |
|---|---|---|
| **Supply chain / reverse factoring** | Payable days rise; debt unchanged | Bank financing of payables |
| **Receivables factoring or discounting** | Receivable days fall; cash rises | Receivables sold, sometimes with recourse |
| **Bill discounting** | Similar to factoring | Common in Indian manufacturing |
| **Channel financing** | Distributor is financed by a bank, not by the company | Company's receivables fall; the credit risk may or may not transfer |
| **Securitisation with recourse** | Assets removed from the balance sheet | Risk retained |
| **Letters of credit for purchases** | Payment deferred | A form of short-term borrowing |

### The detection checks

**1. Payable days rising sharply with no commercial explanation.** A sudden extension of payment terms across a supplier base is unusual unless the company has substantial new bargaining power or has introduced a financing arrangement. Ask which.

**2. Receivable days falling while revenue grows strongly.** Genuine collection improvement is possible; factoring is the alternative explanation and is more common.

**3. Disclosure in the notes.** Accounting standards and disclosure practice increasingly require some disclosure of supply chain finance arrangements. Read the trade payables note, the financial instruments note, and the cash flow classification.

**4. Cash flow statement classification.** Whether the flows are shown as operating or financing is the key question — **classifying a financing arrangement's cash flows as operating inflates operating cash flow**, which undermines the cash-versus-profit integrity test that the forensic chapters rely on.

**5. Interest cost relative to reported debt.** Where finance costs are high relative to disclosed borrowings, off-balance-sheet financing is a candidate explanation, and the reconciliation is worth doing.

**6. Recourse terms.** Factoring without recourse genuinely transfers credit risk; with recourse, the company remains exposed and the receivable has been financed rather than sold.

### Why it matters analytically

- **Leverage is understated.** A company with substantial supply chain finance has borrowings that do not appear in net debt, so EV is understated and leverage ratios flatter.
- **Working capital metrics are not comparable** across companies where one uses these arrangements and another does not — a specific and common peer-comparison error.
- **Operating cash flow may be inflated**, breaking the most important quality-of-earnings check.
- **The facility can be withdrawn.** This is the real risk: supply chain finance is uncommitted in many structures, and a bank reducing the facility forces the company to pay suppliers on original terms immediately — a sudden, large working-capital outflow at exactly the moment the company's credit is being questioned. **This reflexivity has caused severe distress episodes internationally.**

### The adjustment

Where the arrangements are material and disclosed:
1. **Reclassify** the financed payables as debt.
2. **Recompute net debt, leverage and enterprise value.**
3. **Restate working capital days** on a comparable basis.
4. **Reclassify the cash flows** to financing if they have been shown as operating.
5. **State the adjustment** in the note, since your figures will differ from screen data.

Where disclosure is insufficient to quantify it, **say so explicitly** — flagging an unquantifiable exposure is more useful than ignoring it.

### The legitimate side

These arrangements are not inherently improper, and a balanced treatment says so:
- **Suppliers benefit** from early payment at a rate based on the buyer's stronger credit rather than their own — genuinely useful for small suppliers.
- **The company benefits** from extended terms at a lower cost than direct borrowing.
- **The problem is presentational**, not the arrangement itself: when the economics are borrowing and the presentation is trade credit, the analyst must adjust.

### Related working capital financing questions

- **Working capital facility utilisation** — rising utilisation of sanctioned limits is an early cash-strain signal, per the credit chapter, and is disclosed.
- **Seasonal peak working capital** may be far above the year-end figure, so the year-end borrowing level understates the peak requirement. **Ask about peak utilisation**, which the year-end balance sheet does not show.
- **Inventory funding** through supplier consignment arrangements, where stock sits with the company but is owned by the supplier — reduces reported inventory without changing the operation.
- **Advance from customers** as a funding source, common in capital goods and real estate, which is genuine negative working capital and a real competitive advantage where it exists.

## Common mistakes
- Reading a **payable-days extension** as improved bargaining power without checking for a financing arrangement.
- Treating **factored receivables** as collected.
- Ignoring **recourse** terms, which determine whether risk actually transferred.
- Comparing working capital metrics across companies with **different financing arrangements**.
- Accepting **operating cash flow** that includes financing-arrangement inflows.
- Ignoring the **withdrawal risk** of an uncommitted facility.
- Using the **year-end** working capital position as the peak requirement.
- Treating these arrangements as inherently improper rather than as a presentation issue requiring adjustment.

## Interview angle
"Payable days went from 58 to 96 in a year. What do you conclude?" Do not assume improved bargaining power — the more likely explanation is a supply chain finance arrangement, where a bank pays the suppliers early and the company repays the bank on extended terms, which is economically borrowing presented as trade credit. Say what you would check: the trade payables and financial instruments notes for disclosure of such arrangements, the cash flow statement for whether the flows are classified as operating or financing, and finance costs against disclosed borrowings, since a mismatch points to off-balance-sheet funding. Then give the adjustment: reclassify the financed payables as debt, recompute net debt and leverage, and restate working capital days so the comparison against peers is meaningful. Finish with the risk that makes it more than a presentation issue — these facilities are frequently uncommitted, so a bank reducing the line forces immediate payment to suppliers on original terms, producing a large working-capital outflow at exactly the moment the company's credit is already being questioned.
