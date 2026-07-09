"""Tests for document loading, cleaning, and chunking."""
import unittest

from rag.ingest import Chunk, chunk_text, clean_text


class TestClean(unittest.TestCase):
    def test_strips_markdown_and_collapses_whitespace(self):
        raw = "# Title\n\nSome **bold** text.\n\n- bullet one\n- bullet two\n"
        cleaned = clean_text(raw)
        self.assertNotIn("#", cleaned)
        self.assertNotIn("**", cleaned)
        self.assertNotIn("\n", cleaned)
        self.assertIn("Some bold text.", cleaned)
        self.assertIn("bullet one", cleaned)

    def test_removes_code_fences(self):
        raw = "Intro text.\n```python\nprint('hi')\n```\nOutro text."
        cleaned = clean_text(raw)
        self.assertIn("Intro text.", cleaned)
        self.assertIn("Outro text.", cleaned)
        self.assertNotIn("print", cleaned)


class TestChunking(unittest.TestCase):
    def test_chunk_overlap_and_span(self):
        words = " ".join(f"w{i}" for i in range(100))
        chunks = chunk_text(words, source="doc.md", chunk_size=40, overlap=10)
        # step = 30 -> windows [0:40], [30:70], [60:100] => 3 chunks
        self.assertEqual(len(chunks), 3)
        self.assertIsInstance(chunks[0], Chunk)
        self.assertEqual(chunks[0].start_word, 0)
        self.assertEqual(chunks[0].end_word, 40)
        # consecutive chunks overlap by exactly `overlap` words
        self.assertEqual(chunks[1].start_word, 30)
        overlap_words = set(chunks[0].text.split()) & set(chunks[1].text.split())
        self.assertEqual(len(overlap_words), 10)

    def test_chunk_ids_unique_and_ordered(self):
        words = " ".join(f"w{i}" for i in range(50))
        chunks = chunk_text(words, source="a.md", chunk_size=20, overlap=5)
        ids = [c.chunk_id for c in chunks]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(chunks[0].chunk_id, "a.md#0")

    def test_short_text_single_chunk(self):
        chunks = chunk_text("just a few words here", source="s.md", chunk_size=120, overlap=30)
        self.assertEqual(len(chunks), 1)
        self.assertEqual(chunks[0].end_word, 5)

    def test_empty_text_no_chunks(self):
        self.assertEqual(chunk_text("", source="e.md"), [])

    def test_invalid_overlap_raises(self):
        with self.assertRaises(ValueError):
            chunk_text("a b c", source="x.md", chunk_size=10, overlap=10)


if __name__ == "__main__":
    unittest.main()
