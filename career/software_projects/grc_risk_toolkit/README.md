# GRC Control & Risk-Register Toolkit

A small Governance-Risk-Compliance workflow in one readable Python file:
1. **Risk register** — Likelihood x Impact scoring, rating, owner, treatment, status.
2. **ISO 27001:2022 Annex A control mapping** — each risk mapped to a control theme with coverage status.
3. **Vendor / third-party security questionnaire** — weighted answers scored into a risk tier (due-diligence review).

Outputs an Excel workbook (Risk_Register / Control_Mapping / Vendor_Assessment) and a 5x5 risk heat-map.
See **[STUDY_GUIDE.md](STUDY_GUIDE.md)** for the plain-English explanation and interview Q&A.

## Run it
```bash
pip install pandas openpyxl matplotlib
python main.py
```
Built for a **GRC / Security Risk & Compliance Analyst** portfolio.
