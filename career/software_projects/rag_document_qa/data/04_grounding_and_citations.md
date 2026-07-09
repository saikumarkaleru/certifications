# Grounding and Citations

Grounding means constraining a language model to answer only from a specific set
of retrieved passages rather than from its own memory. The retrieved chunks are
inserted into the prompt, and the model is instructed to use only that context.

Citations are the visible evidence of grounding. Each retrieved chunk is given a
numbered marker, and the model is asked to reference those markers in its answer.
Because every claim can be traced back to a source chunk, a reader can verify the
answer instead of trusting it blindly. This auditability is one of the biggest
practical advantages of RAG over a bare language model.

A grounded prompt typically has three parts: an instruction that tells the model
to answer only from the context and to admit when it does not know, a context
block that lists the numbered source chunks, and the user's question. Keeping the
instruction explicit about refusing to answer beyond the context is what reduces
fabrication.
