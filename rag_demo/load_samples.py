"""
Pre-seed rag.db with the sample documents.

Reads every markdown file in sample_docs/, uses the filename (without .md) as the
`source`, and ingests it through the same pipeline the API uses. Existing chunks are
cleared first, so this is safe to re-run before a demo.

Run from the rag_demo/ folder:
    uv run python load_samples.py

Requires OPENROUTER_API_KEY in .env (embeddings are computed via OpenRouter).
"""

import glob
import os

from sqlalchemy import text

import main
from main import ingest, DocumentIn, SessionLocal, Chunk

DOCS_DIR = os.path.join(os.path.dirname(__file__), "sample_docs")


def reset():
    """Remove all existing chunks and their vectors."""
    db = SessionLocal()
    try:
        db.execute(text("DELETE FROM vec_chunks"))
        db.query(Chunk).delete()
        db.commit()
    finally:
        db.close()


def run():
    if not main.OPENROUTER_API_KEY:
        print("OPENROUTER_API_KEY is not set. Add it to rag_demo/.env and retry.")
        return

    paths = sorted(glob.glob(os.path.join(DOCS_DIR, "*.md")))
    if not paths:
        print(f"No .md files found in {DOCS_DIR}")
        return

    reset()
    print("Cleared existing chunks.")

    total = 0
    for path in paths:
        source = os.path.splitext(os.path.basename(path))[0]
        with open(path, encoding="utf-8") as f:
            content = f.read()

        db = SessionLocal()
        try:
            result = ingest(DocumentIn(source=source, text=content), db=db)
            print(f"  {source}: {result.chunks_created} chunks")
            total += result.chunks_created
        finally:
            db.close()

    print(f"Done. Ingested {len(paths)} documents, {total} chunks total.")


if __name__ == "__main__":
    run()
