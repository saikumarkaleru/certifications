# Retrieval-Augmented Generation (RAG)

Retrieval-Augmented Generation, or RAG, is a technique for grounding a large
language model in an external body of knowledge. Instead of relying only on the
facts baked into the model's weights during training, a RAG system first
retrieves relevant passages from a document collection and then asks the model
to answer using those passages as context.

A RAG pipeline has two stages. The first stage is retrieval: given a user
question, the system searches an index of document chunks and returns the most
relevant ones. The second stage is generation: the retrieved chunks are placed
into the prompt, and the language model produces an answer grounded in that
context.

The main benefit of retrieval-augmented generation is that it lets a model
answer questions about private, recent, or domain-specific information that was
never part of its training data. It also reduces hallucination, because the
model is instructed to answer only from the supplied context, and it makes
answers auditable through citations back to the source documents.
