"""End-to-end tests for the RAG pipeline with MockLLM (no API key)."""
import unittest
from pathlib import Path

from rag.ingest import ingest_directory
from rag.llm import MockLLM, get_provider
from rag.pipeline import RAGPipeline
from rag.vectorstore import build_retriever

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


class TestMockLLM(unittest.TestCase):
    def test_extractive_answer_uses_context(self):
        llm = MockLLM()
        context = (
            "RAG grounds a model in external knowledge. "
            "Chunking splits documents into pieces. "
            "Cosine similarity measures vector closeness."
        )
        out = llm.generate("", "What does chunking do?", context)
        self.assertIn("Chunking", out)

    def test_deterministic(self):
        llm = MockLLM()
        ctx = "Alpha beta gamma. The delta epsilon zeta. Interest rates fell."
        a = llm.generate("", "interest rates", ctx)
        b = llm.generate("", "interest rates", ctx)
        self.assertEqual(a, b)


class TestPipelineEndToEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chunks = ingest_directory(DATA_DIR)
        cls.pipeline = RAGPipeline(
            retriever=build_retriever("tfidf"),
            provider=get_provider("mock"),
            top_k=3,
        ).index_chunks(cls.chunks)

    def test_data_ingested(self):
        self.assertGreater(len(self.chunks), 0)
        sources = {c.source for c in self.chunks}
        self.assertGreaterEqual(len(sources), 4)

    def test_answers_rag_question_with_sources(self):
        ans = self.pipeline.ask("What is retrieval-augmented generation?")
        self.assertTrue(ans.answer)
        self.assertTrue(ans.sources)
        # The retrieved sources should include the RAG intro doc.
        srcs = {s.source for s in ans.sources}
        self.assertIn("01_what_is_rag.md", srcs)
        # Markers are 1-indexed and contiguous.
        self.assertEqual([s.marker for s in ans.sources], list(range(1, len(ans.sources) + 1)))

    def test_answers_tfidf_question_grounded(self):
        ans = self.pipeline.ask("What is the difference between TF-IDF and dense embeddings?")
        self.assertTrue(ans.sources)
        top_source = ans.sources[0].source
        self.assertEqual(top_source, "03_tfidf_vs_embeddings.md")

    def test_provider_name_reported(self):
        ans = self.pipeline.ask("How does overlap help chunking?")
        self.assertEqual(ans.provider, "mock")

    def test_ask_before_index_raises(self):
        p = RAGPipeline(retriever=build_retriever("tfidf"), provider=get_provider("mock"))
        with self.assertRaises(RuntimeError):
            p.ask("anything")

    def test_prompt_contains_numbered_sources(self):
        retrieved = self.pipeline.retriever.query("citations grounding", top_k=2)
        prompt, context = RAGPipeline.build_prompt("q?", retrieved)
        self.assertIn("[1]", prompt)
        self.assertIn("Question: q?", prompt)


class TestProviderSelection(unittest.TestCase):
    def test_default_is_mock(self):
        self.assertIsInstance(get_provider("mock"), MockLLM)

    def test_unknown_provider_raises(self):
        with self.assertRaises(ValueError):
            get_provider("does-not-exist")


if __name__ == "__main__":
    unittest.main()
