# Hallucination Mitigation and Evaluation

A hallucination is a confident but incorrect statement produced by a language
model, typically a fact that is not supported by any source. RAG reduces
hallucination by supplying trustworthy context and instructing the model to
answer only from it, but it does not eliminate the risk entirely.

Several techniques reduce hallucination further. Retrieving enough relevant
context so the answer is actually present is the first line of defence. Telling
the model to say "I don't know" when the context is insufficient prevents it from
inventing an answer. Lowering the sampling temperature makes output more
deterministic and conservative. Requiring citations forces the model to point at
evidence, which discourages unsupported claims.

Evaluating a RAG system has two halves. Retrieval quality asks whether the right
chunks were fetched, measured with metrics such as recall at k, which checks
whether a relevant chunk appears in the top k results, and mean reciprocal rank,
which rewards placing the best chunk near the top. Answer quality asks whether the
final response is correct and grounded, measured by faithfulness, which checks
that every claim is supported by the retrieved context, and answer relevance,
which checks that the response actually addresses the question.

A simple offline evaluation builds a small set of question and expected-answer
pairs, runs them through the pipeline, and checks that the expected facts appear
in the generated answer and that the citations point to the correct source.
