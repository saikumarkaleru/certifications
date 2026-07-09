# TF-IDF versus Dense Embeddings

Retrieval systems need a way to measure how relevant a chunk is to a question.
Two common families of methods are sparse lexical scoring, such as TF-IDF, and
dense vector embeddings.

TF-IDF stands for term frequency inverse document frequency. It scores a chunk
by how often the question's words appear in it, weighted so that rare, informative
words count more than common words. TF-IDF is fast, transparent, and requires no
training or model download, which makes it an excellent default and a strong
baseline. Its weakness is that it matches on exact words and cannot tell that
"car" and "automobile" mean the same thing.

Dense embeddings map text into a vector of a few hundred numbers using a neural
network such as a sentence transformer. Two passages that mean similar things end
up close together in vector space even if they share no words, so embeddings
capture semantic similarity. The cost is that you must download a model, run it
to encode every chunk, and store the vectors.

Similarity between two vectors is usually measured with cosine similarity, which
is the dot product of the two vectors divided by the product of their lengths.
Cosine similarity ranges from zero for unrelated text to one for identical
direction, and it is used by both TF-IDF and dense-embedding retrievers.

A practical system often starts with TF-IDF for its simplicity and later swaps in
dense embeddings, or combines the two in a hybrid retriever, once semantic recall
becomes important.
