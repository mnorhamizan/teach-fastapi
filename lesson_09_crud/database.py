"""
DATABASE CONFIGURATION
=======================
This file sets up the SQLAlchemy database connection.

SQLAlchemy is an ORM (Object-Relational Mapper) that lets you:
- Define database tables as Python classes
- Query the database using Python code instead of raw SQL
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ============================================
# STEP 1: Database URL
# ============================================
# SQLite database - creates a file called 'items.db'
# For production, you would use PostgreSQL, MySQL, etc.
SQLALCHEMY_DATABASE_URL = "sqlite:///./items.db"

# PostgreSQL example (for reference):
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"


# ============================================
# STEP 2: Create Engine
# ============================================
# The engine is the starting point for SQLAlchemy
# It manages the database connection

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Needed for SQLite only
)


# ============================================
# STEP 3: Create Session Factory
# ============================================
# Sessions are used to interact with the database
# Each request gets its own session

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# ============================================
# STEP 4: Create Base Class
# ============================================
# All our database models will inherit from this base class

Base = declarative_base()


# ============================================
# STEP 5: Dependency for FastAPI
# ============================================
# This function creates a new database session for each request
# and closes it when the request is done

def get_db():
    """
    Dependency that provides a database session.

    Usage in FastAPI:
        @app.get("/items")
        def get_items(db: Session = Depends(get_db)):
            ...
    """
    db = SessionLocal()
    try:
        yield db  # Provide the session to the endpoint
    finally:
        db.close()  # Always close when done
