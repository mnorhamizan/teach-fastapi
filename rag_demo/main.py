"""
RAG DEMO — two pipelines with sqlite-vec + OpenRouter
=====================================================
Level: Intermediate (companion demo to the FastAPI course)

This shows the whole Retrieval-Augmented Generation loop in two endpoints,
using the same stack as the course (FastAPI + SQLAlchemy + SQLite + OpenRouter):

    Pipeline 1 — INGEST   (POST /rag/documents)
        text -> chunk -> embed -> store vectors in SQLite (sqlite-vec)

    Pipeline 2 — RETRIEVE + COMPLETE   (POST /rag/query)
        question -> embed -> KNN search -> stuff context -> LLM answer

Storage: vectors live in a `vec0` virtual table (sqlite-vec) and the chunk text
lives in a normal SQLAlchemy table, joined by id.

Installation:
    uv sync

Environment:
    Put OPENROUTER_API_KEY in a .env file.

To run:
    uv run uvicorn main:app --reload

API Docs: http://127.0.0.1:8000/docs
"""

import os
from typing import Optional

import sqlite_vec
from sqlite_vec import serialize_float32
from dotenv import load_dotenv
from openai import OpenAI
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from sqlalchemy import create_engine, event, Column, Integer, String, Text, text
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session

load_dotenv()


# ============================================
# Configuration
# ============================================

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

EMBED_MODEL = "qwen/qwen3-embedding-4b"   # served by OpenRouter
EMBED_DIM = 2560                          # Qwen3-Embedding-4B output dimension
CHAT_MODEL = "minimax/minimax-m2.5"

TOP_K = 4            # how many chunks to retrieve per query
CHUNK_SIZE = 500     # characters per chunk
CHUNK_OVERLAP = 50   # characters of overlap between consecutive chunks

# One client for BOTH embeddings and completion (OpenRouter is OpenAI-compatible).
# Built only when a key is present so the app can still start without one
# (endpoints then return a clean 500 via require_key()).
client = OpenAI(base_url=OPENROUTER_BASE_URL, api_key=OPENROUTER_API_KEY) if OPENROUTER_API_KEY else None


# ============================================
# Database setup (SQLAlchemy + sqlite-vec)
# ============================================

engine = create_engine(
    "sqlite:///./rag.db",
    connect_args={"check_same_thread": False},
)


# Load the sqlite-vec extension on every new connection. This is what gives
# SQLite the `vec0` virtual table and the KNN `MATCH` operator.
@event.listens_for(engine, "connect")
def _load_sqlite_vec(dbapi_conn, _connection_record):
    dbapi_conn.enable_load_extension(True)
    sqlite_vec.load(dbapi_conn)
    dbapi_conn.enable_load_extension(False)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class Chunk(Base):
    """The text of each chunk. Vectors are stored separately in `vec_chunks`."""
    __tablename__ = "chunks"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)


Base.metadata.create_all(bind=engine)

# Create the vec0 virtual table once, at startup. `distance_metric=cosine` means
# a smaller distance == more similar. The dimension is fixed here for the life of
# the table (same rule as the embedding model: can't change without re-indexing).
with engine.begin() as _conn:
    _conn.exec_driver_sql(
        "CREATE VIRTUAL TABLE IF NOT EXISTS vec_chunks USING vec0("
        f"  chunk_id integer primary key,"
        f"  embedding float[{EMBED_DIM}] distance_metric=cosine"
        ")"
    )


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ============================================
# Core RAG helpers
# ============================================

def chunk_text(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    """Split text into overlapping fixed-size windows.

    Deliberately simple (character windows). Production systems chunk on
    sentence/token boundaries instead — but this keeps the mechanic obvious.
    """
    text = text.strip()
    chunks: list[str] = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + size])
        start += size - overlap
    return [c for c in chunks if c.strip()]


def embed(texts: list[str]) -> list[list[float]]:
    """Turn texts into vectors via OpenRouter (batched in one call)."""
    resp = client.embeddings.create(model=EMBED_MODEL, input=texts)
    return [item.embedding for item in resp.data]


def complete(question: str, context: str) -> str:
    """Ask the LLM to answer the question using only the retrieved context."""
    resp = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant. Answer the question using ONLY the "
                    "provided context. If the answer is not in the context, say you "
                    "don't know."
                ),
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {question}",
            },
        ],
    )
    return resp.choices[0].message.content


def require_key():
    if not OPENROUTER_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="OPENROUTER_API_KEY is not set. Add it to a .env file.",
        )


# ============================================
# Schemas
# ============================================

class DocumentIn(BaseModel):
    source: str = "untitled"
    text: str


class IngestResponse(BaseModel):
    source: str
    chunks_created: int


class QueryIn(BaseModel):
    question: str
    k: Optional[int] = None


class Source(BaseModel):
    content: str
    distance: float


class QueryResponse(BaseModel):
    question: str
    answer: str
    sources: list[Source]


# ============================================
# App + endpoints
# ============================================

app = FastAPI(
    title="RAG Demo",
    description="Two pipelines: ingest, and retrieve + complete (sqlite-vec + OpenRouter)",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "demo": "RAG with sqlite-vec + OpenRouter",
        "ingest": "POST /rag/documents",
        "query": "POST /rag/query",
        "docs": "/docs",
    }


# ---- Pipeline 1: INGEST ----
@app.post("/rag/documents", response_model=IngestResponse)
def ingest(doc: DocumentIn, db: Session = Depends(get_db)):
    """
    Ingest a document: chunk it, embed each chunk, and store the vectors.

    - **source**: a label for where the text came from
    - **text**: the raw text to index
    """
    require_key()

    chunks = chunk_text(doc.text)
    if not chunks:
        raise HTTPException(status_code=400, detail="No text to ingest.")

    vectors = embed(chunks)
    if len(vectors[0]) != EMBED_DIM:
        raise HTTPException(
            status_code=500,
            detail=(
                f"Embedding dim {len(vectors[0])} != configured EMBED_DIM {EMBED_DIM}. "
                f"Set EMBED_DIM = {len(vectors[0])} and delete rag.db, then retry."
            ),
        )

    for content, vec in zip(chunks, vectors):
        row = Chunk(source=doc.source, content=content)
        db.add(row)
        db.flush()                   # assigns row.id without committing yet
        db.execute(
            text("INSERT INTO vec_chunks(chunk_id, embedding) VALUES (:cid, :emb)"),
            {"cid": row.id, "emb": serialize_float32(vec)},
        )

    db.commit()
    return IngestResponse(source=doc.source, chunks_created=len(chunks))


# ---- Pipeline 2: RETRIEVE + COMPLETE ----
@app.post("/rag/query", response_model=QueryResponse)
def query(q: QueryIn, db: Session = Depends(get_db)):
    """
    Answer a question over the ingested documents.

    Embeds the question, finds the nearest chunks (KNN), stuffs them into the
    prompt as context, and asks the LLM to answer.
    """
    require_key()
    k = q.k or TOP_K

    query_vec = embed([q.question])[0]

    rows = db.execute(
        text(
            "SELECT chunk_id, distance FROM vec_chunks "
            "WHERE embedding MATCH :q ORDER BY distance LIMIT :k"
        ),
        {"q": serialize_float32(query_vec), "k": k},
    ).fetchall()

    if not rows:
        raise HTTPException(
            status_code=404,
            detail="No relevant chunks found. Ingest documents via POST /rag/documents first.",
        )

    distance_by_id = {chunk_id: dist for chunk_id, dist in rows}
    found = db.query(Chunk).filter(Chunk.id.in_(list(distance_by_id))).all()
    found.sort(key=lambda c: distance_by_id[c.id])   # nearest first

    context = "\n\n".join(c.content for c in found)
    answer = complete(q.question, context)

    sources = [
        Source(content=c.content, distance=round(distance_by_id[c.id], 4))
        for c in found
    ]
    return QueryResponse(question=q.question, answer=answer, sources=sources)
