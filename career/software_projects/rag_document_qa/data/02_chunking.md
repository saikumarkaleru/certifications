# Document Chunking

Chunking is the process of splitting long documents into smaller pieces before
they are indexed for retrieval. Language models and retrievers work best with
focused passages, so a large document is divided into chunks of a few hundred
words each.

Chunk size is a trade-off. Chunks that are too large dilute the signal, because
a single chunk may cover several unrelated topics and the relevant sentence is
buried among noise. Chunks that are too small lose context, because an answer
that spans several sentences may be split across chunk boundaries and never
retrieved together.

Overlap between chunks addresses the boundary problem. By letting consecutive
chunks share a number of words, an idea that falls near the edge of one chunk
also appears in the next chunk, so it is not lost at retrieval time. A common
setting is a chunk size of one to two hundred words with an overlap of ten to
thirty percent.

Every chunk should carry metadata: the source document it came from, its
position within that document, and any section titles. This metadata is what
makes citation possible, so the final answer can point back to exactly where
each fact was found.
