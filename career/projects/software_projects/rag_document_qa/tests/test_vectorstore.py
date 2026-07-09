"""Tests for the pure-Python TF-IDF retriever."""
import unittest

from rag.ingest import Chunk
from rag.vectorstore import TfidfRetriever, build_retriever, tokenize


def _mk(text, i):
    return Chunk(text=text, source="d.md", chunk_index=i, start_word=0, end_word=0)


class TestTokenize(unittest.TestCase):
    def test_lowercases_and_drops_stopwords(self):
        toks = tokenize("The Cat and the Dog RAN")
        self.assertIn("cat", toks)
        self.assertIn("dog", toks)
        self.assertIn("ran", toks)
        self.assertNotIn("the", toks)
        self.assertNotIn("and", toks)


class TestTfidfRetriever(unittest.TestCase):
    def setUp(self):
        self.chunks = [
            _mk("The stock market rallied as interest rates fell sharply.", 0),
            _mk("Photosynthesis converts sunlight into chemical energy in plants.", 1),
            _mk("Bond yields rise when interest rates increase over time.", 2),
            _mk("The chef prepared a delicious pasta with fresh tomatoes.", 3),
        ]
        self.r = TfidfRetriever().fit(self.chunks)

    def test_retrieves_relevant_chunk_first(self):
        results = self.r.query("What happens to interest rates and bond yields?", top_k=2)
        self.assertTrue(results)
        top_text = results[0][0].text
        # The most relevant chunk should mention interest rates / yields.
        self.assertTrue("yields" in top_text or "interest rates" in top_text)

    def test_scores_sorted_descending(self):
        results = self.r.query("interest rates", top_k=4)
        scores = [s for _, s in results]
        self.assertEqual(scores, sorted(scores, reverse=True))
        self.assertTrue(all(s > 0 for s in scores))

    def test_unrelated_query_returns_no_or_low_matches(self):
        results = self.r.query("quantum entanglement of qubits", top_k=4)
        # None of the corpus words overlap -> empty result.
        self.assertEqual(results, [])

    def test_top_k_respected(self):
        results = self.r.query("interest rates market energy pasta", top_k=2)
        self.assertLessEqual(len(results), 2)

    def test_empty_index(self):
        r = TfidfRetriever().fit([])
        self.assertEqual(r.query("anything", top_k=3), [])

    def test_query_before_fit_raises(self):
        with self.assertRaises(RuntimeError):
            TfidfRetriever().query("x")

    def test_factory_returns_tfidf(self):
        self.assertIsInstance(build_retriever("tfidf"), TfidfRetriever)
        with self.assertRaises(ValueError):
            build_retriever("nonsense")


if __name__ == "__main__":
    unittest.main()
