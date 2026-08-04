// Merge the Stock-Market-Roles-Master_FULL.pdf from its component PDFs.
// Prerequisite: npm install pdf-lib   (run once, in this folder or any ancestor)
// Usage: node merge_stock_market_master.mjs
// Rebuild after any component PDF changes (front matter, or any of the sources below).

import { PDFDocument } from "pdf-lib";
import fs from "node:fs";

const STUDY = "C:/Users/saikumarkaleru/Desktop/certifications/study";
const BASE = `${STUDY}/Finance`;
const SOURCES = [
  `${BASE}/sources_md/_frontmatter.pdf`,
  `${BASE}/05_Equity_and_Capital_Markets.pdf`,
  `${BASE}/_components/Valuation_FULL.pdf`,
  `${BASE}/_components/Investments-Portfolio-Management_FULL.pdf`,
  `${BASE}/Technical_Research_Study_Guide.pdf`,
  `${BASE}/Technical_Research_Deepening_Handbook.pdf`,
  `${STUDY}/trading_learning/Technical-Analysis-Complete_FULL.pdf`,
  `${STUDY}/trading_learning/Options-Trading-Complete_FULL.pdf`,
  `${BASE}/Market_Research_Study_Guide.pdf`,
];
const OUT = `${BASE}/Stock-Market-Roles-Master_FULL.pdf`;

const merged = await PDFDocument.create();
merged.setTitle("Stock Market Roles Master Study Guide");
merged.setAuthor("Saikumar Kaleru");

for (const src of SOURCES) {
  const bytes = fs.readFileSync(src);
  const doc = await PDFDocument.load(bytes, { updateMetadata: false });
  const pages = await merged.copyPages(doc, doc.getPageIndices());
  for (const p of pages) merged.addPage(p);
  console.log(`+ ${pages.length} pages from ${src.split("/").pop()}`);
}

const outBytes = await merged.save();
fs.writeFileSync(OUT, outBytes);
console.log(`\nDONE -> ${OUT}`);
console.log(`total pages: ${merged.getPageCount()}`);
console.log(`size: ${(outBytes.length / 1024 / 1024).toFixed(2)} MB`);
