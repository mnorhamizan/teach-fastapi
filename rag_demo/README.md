# RAG Demo — two pipelines with sqlite-vec + OpenRouter

A minimal, readable Retrieval-Augmented Generation demo built on the same stack as
the course (FastAPI + SQLAlchemy + SQLite + OpenRouter). It shows the whole RAG
loop in two endpoints:

1. **Ingest** — `POST /rag/documents`: text → chunk → embed → store vectors in SQLite (`sqlite-vec`)
2. **Retrieve + complete** — `POST /rag/query`: question → embed → KNN search → stuff context → LLM answer

## Setup

```bash
cd rag_demo
uv sync
echo "OPENROUTER_API_KEY=sk-or-..." > .env   # your OpenRouter key
```

## Run

```bash
uv run uvicorn main:app --reload
```

Then open http://127.0.0.1:8000/docs and:

1. `POST /rag/documents` with some text (paste a few paragraphs).
2. `POST /rag/query` with a question about that text.

## Models (OpenRouter)

- Embeddings: `qwen/qwen3-embedding-4b` (2560-dim)
- Completion: `minimax/minimax-m2.5`

Both run through OpenRouter's OpenAI-compatible API with a single `OPENROUTER_API_KEY`.
