"""
DATABASE MODELS (SQLAlchemy ORM)
=================================
This file defines the database tables as Python classes.

Each class = One database table
Each attribute = One column in the table
"""

from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.sql import func
from database import Base


# ============================================
# Item Model
# ============================================
# This creates a table called "items" in the database

class Item(Base):
    """
    Item table in the database.

    Columns:
        - id: Primary key (auto-generated)
        - name: Item name (required)
        - description: Item description (optional)
        - price: Item price (required)
        - quantity: Stock quantity (default: 0)
        - is_available: Whether item is available (default: True)
        - created_at: Timestamp when created (auto-generated)
        - updated_at: Timestamp when updated (auto-updated)
    """

    # Table name in the database
    __tablename__ = "items"

    # Columns
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    description = Column(String(500), nullable=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, default=0)
    is_available = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


# ============================================
# COLUMN TYPES REFERENCE
# ============================================
"""
Common SQLAlchemy column types:

| SQLAlchemy Type | Python Type | Description          |
|-----------------|-------------|----------------------|
| Integer         | int         | Whole numbers        |
| String(length)  | str         | Text with max length |
| Text            | str         | Unlimited text       |
| Float           | float       | Decimal numbers      |
| Boolean         | bool        | True/False           |
| DateTime        | datetime    | Date and time        |
| Date            | date        | Date only            |

Column options:
- primary_key=True  : Makes this the primary key
- nullable=False    : Cannot be NULL (required)
- default=value     : Default value if not provided
- index=True        : Creates database index (faster queries)
- unique=True       : Value must be unique
"""
