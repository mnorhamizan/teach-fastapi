"""
PYDANTIC SCHEMAS
=================
Request and response schemas for the Todo API.
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TodoCreate(BaseModel):
    """Schema for creating a new todo."""
    title: str
    description: Optional[str] = None
    priority: int = 1  # 1=Low, 2=Medium, 3=High


class TodoUpdate(BaseModel):
    """Schema for updating a todo."""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[int] = None


class TodoResponse(BaseModel):
    """Schema for todo response."""
    id: int
    title: str
    description: Optional[str] = None
    completed: bool
    priority: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
