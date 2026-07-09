# Minimal image for the RAG document-QA system.
# The core pipeline is stdlib-only, so no pip install is needed to run the demo
# or the tests. Optional extras (FastAPI, OpenAI, Anthropic) can be layered in
# by uncommenting the pip line below.
FROM python:3.12-slim

WORKDIR /app

# Copy the project.
COPY . /app

# OPTIONAL extras — the default build stays dependency-free:
# RUN pip install --no-cache-dir -r requirements.txt

# Sanity-check the build: compile everything and run the offline test suite.
RUN python -m py_compile rag/*.py api.py tests/*.py \
    && python -m unittest discover -s tests

# Default command: run the end-to-end demo against the bundled sample docs.
CMD ["python", "-m", "rag.cli", "demo", "data"]
