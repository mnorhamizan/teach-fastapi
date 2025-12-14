"""
PYDANTIC SCHEMAS
=================
These are the request/response models for the API.

Why separate from SQLAlchemy models?
- SQLAlchemy models = How data is stored in database
- Pydantic schemas = How data is sent/received via API

This separation gives you control over what data is exposed.
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# ============================================
# Request Schemas (Input)
# ============================================

class ItemCreate(BaseModel):
    """Schema for creating a new item."""
    name: str
    description: Optional[str] = None
    price: float
    quantity: int = 0
    is_available: bool = True


class ItemUpdate(BaseModel):
    """Schema for updating an item. All fields optional."""
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    is_available: Optional[bool] = None


# ============================================
# Response Schemas (Output)
# ============================================

class ItemResponse(BaseModel):
    """Schema for item response."""
    id: int
    name: str
    description: Optional[str] = None
    price: float
    quantity: int
    is_available: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        """Enable ORM mode to work with SQLAlchemy models."""
        from_attributes = True  # Pydantic v2 (use orm_mode = True for v1)


# ============================================
# WHY USE from_attributes = True?
# ============================================
"""
By default, Pydantic expects dict input:
    ItemResponse(**{"id": 1, "name": "Laptop", ...})

With from_attributes = True, it can read from SQLAlchemy objects:
    ItemResponse.model_validate(sqlalchemy_item)

This is essential for FastAPI + SQLAlchemy integration!
"""
