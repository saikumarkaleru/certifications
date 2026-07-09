# Core toolkit is stdlib-only, so the base image needs no pip install to run
# the CLI and tests. Optional extras (openai/anthropic/fastapi) can be added
# by uncommenting the pip line below.
FROM python:3.12-slim

WORKDIR /app
COPY . /app

# Optional: install real-LLM / API extras.
# RUN pip install --no-cache-dir -r requirements.txt

# Run the test suite at build time as a smoke check (stdlib only).
RUN python -m unittest discover -s tests -p "test_*.py"

# Default: run the demo task with the offline MockLLM (no API key needed).
ENTRYPOINT ["python", "-m", "agent.cli"]
CMD ["what is 12*(3+4)?"]
